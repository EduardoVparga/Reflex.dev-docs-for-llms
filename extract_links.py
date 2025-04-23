import sys
import time
import logging
from pathlib import Path
from typing import List, Set

from selenium import webdriver
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.firefox.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from bs4 import BeautifulSoup

# Optionally use webdriver_manager to handle geckodriver installation
# from webdriver_manager.firefox import GeckoDriverManager

# Constants
CHEVRON_BUTTON_XPATH = (
    "//button[.//*[@class='lucide lucide-chevron-down size-4 AccordionChevron css-svt5ra']]"
)
LOG_FILE = "scraper.log"
OUTPUT_FILE = "links.txt"
ZOOM_LEVEL = 20 
DRIVER_PATH = Path("./geckodriver")


def setup_logging() -> None:
    """
    Configure logging to output to stdout and to a file.
    """
    logging.basicConfig(
        level=logging.INFO,
        format="%(asctime)s %(levelname)s %(name)s: %(message)s",
        handlers=[
            logging.StreamHandler(sys.stdout),
            logging.FileHandler(LOG_FILE, encoding="utf-8"),
        ],
    )


def create_webdriver(headless: bool = True) -> webdriver.Firefox:
    """
    Initialize and return a headless Firefox WebDriver instance.
    """
    options = Options()
    options.headless = headless

    # If using webdriver_manager:
    # driver = webdriver.Firefox(
    #     executable_path=GeckoDriverManager().install(), options=options
    # )
    service = Service(executable_path=str(DRIVER_PATH))
    driver = webdriver.Firefox(service=service, options=options)
    driver.maximize_window()

    # Apply zoom level
    driver.execute_script(f"document.body.style.zoom='{ZOOM_LEVEL}%'")
    return driver


def scrape_page(driver: webdriver.Firefox, url: str) -> Set[str]:
    """
    Load a page, expand accordions, and extract internal documentation links.
    """
    logging.info(f"Processing URL: {url}")
    found: Set[str] = set()

    driver.get(url)

    try:
        # Wait for accordion chevron buttons to be present
        WebDriverWait(driver, 10).until(
            EC.presence_of_all_elements_located((By.XPATH, CHEVRON_BUTTON_XPATH))
        )

        buttons = driver.find_elements(By.XPATH, CHEVRON_BUTTON_XPATH)
        for btn in buttons:
            try:
                btn.click()
                time.sleep(0.3)
            except Exception as e:
                logging.warning(f"Failed to click button: {e}")

    except Exception as e:
        logging.info(f"No chevrons found or error waiting for elements: {e}")

    # Allow dynamic content to load
    time.sleep(2)

    # Parse page source with BeautifulSoup
    soup = BeautifulSoup(driver.page_source, "html.parser")
    for a_tag in soup.find_all("a", href=True):
        href = a_tag["href"]
        if href.startswith("/docs") and "#" not in href:
            found.add(href)

    logging.info(f"Found {len(found)} links on {url}")
    return found


def save_links(links: Set[str], output_path: str) -> None:
    """
    Save sorted, unique links to a text file.
    """
    path = Path(output_path)
    path.write_text("\n".join(sorted(links)), encoding="utf-8")
    logging.info(f"Saved {len(links)} unique links to {output_path}")


def main(urls: List[str]) -> None:
    setup_logging()
    logging.info("Starting scraper...")

    driver = create_webdriver(headless=True)
    all_links: Set[str] = set()

    try:
        for url in urls:
            links = scrape_page(driver, url)
            all_links.update(links)
    except Exception as e:
        logging.error(f"Unexpected error during scraping: {e}")
    finally:
        driver.quit()
        logging.info("WebDriver has been closed.")

    save_links(all_links, OUTPUT_FILE)
    logging.info("Scraping complete.")


if __name__ == "__main__":
    URLS_TO_SCRAPE = [
        "https://reflex.dev/docs/getting-started/introduction/",
        "https://reflex.dev/docs/library/",
        "https://reflex.dev/docs/hosting/deploy-quick-start/",
        "https://reflex.dev/docs/api-reference/app/",
    ]
    main(URLS_TO_SCRAPE)
