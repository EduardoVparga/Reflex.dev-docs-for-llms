import json
import logging
from pathlib import Path
from typing import List

from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.common.exceptions import TimeoutException, WebDriverException
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.firefox.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from utils import (
    get_last_index,
    set_last_index,
    get_links,
    create_page_sections,
    filename_from_url,
)

# Configuration constants
BASE_URL = "https://reflex.dev"
FILES_DIR = Path("./json_html")
DRIVER_PATH = Path("./geckodriver")
PAGE_LOAD_TIMEOUT = 20
ELEMENT_LOAD_TIMEOUT = 10
SCROLL_PAUSE = 1


def setup_logging() -> None:
    """Configure the logging for the scraper."""
    logging.basicConfig(
        level=logging.INFO,
        format="%(asctime)s [%(levelname)s] %(message)s",
        datefmt="%Y-%m-%d %H:%M:%S",
    )


def setup_driver(headless: bool = False) -> webdriver.Firefox:
    """Initialize and return a Firefox WebDriver instance."""
    options = Options()
    if headless:
        options.add_argument("--headless")
    service = Service(executable_path=str(DRIVER_PATH))

    driver = webdriver.Firefox(service=service, options=options)
    driver.set_page_load_timeout(PAGE_LOAD_TIMEOUT)
    return driver


def fetch_page(driver: webdriver.Firefox, url: str) -> BeautifulSoup:
    """Load a page, wait for rendering, scroll to trigger lazy-loads, and return BeautifulSoup."""
    logging.info(f"Navigating to {url}")
    driver.get(url)

    # Wait for document.readyState == 'complete'
    try:
        WebDriverWait(driver, PAGE_LOAD_TIMEOUT).until(
            lambda d: d.execute_script("return document.readyState") == "complete"
        )
        logging.info("Page fully loaded.")
    except TimeoutException:
        logging.warning("Timeout waiting for full page load.")

    # Wait for the <article> element
    try:
        WebDriverWait(driver, ELEMENT_LOAD_TIMEOUT).until(
            EC.presence_of_element_located((By.TAG_NAME, "article"))
        )
        logging.info("<article> element located.")
    except TimeoutException:
        logging.warning("Timeout waiting for <article> element.")

    # Zoom out to reveal all headers
    try:
        driver.execute_script("document.body.style.zoom = '15%'" )
        WebDriverWait(driver, ELEMENT_LOAD_TIMEOUT).until(
            EC.presence_of_all_elements_located((By.XPATH, "//article//h1 | //article//h2 | //article//h3"))
        )
        logging.info("Headers loaded after zoom.")
    except (WebDriverException, TimeoutException) as e:
        logging.warning(f"Issue during zoom or header wait: {e}")

    # Scroll to load lazy content
    for position, label in [
        (driver.execute_script("return document.body.scrollHeight/2"), "middle"),
        (driver.execute_script("return document.body.scrollHeight"), "bottom"),
    ]:
        try:
            driver.execute_script(f"window.scrollTo(0, {position});")
            logging.info(f"Scrolled to {label} of page.")
            WebDriverWait(driver, SCROLL_PAUSE).until(lambda d: True)
        except WebDriverException as e:
            logging.warning(f"Failed to scroll to {label}: {e}")

    return BeautifulSoup(driver.page_source, "html.parser")


def process_links(links: List[str], start_index: int) -> None:
    """Iterate over links from start_index, fetch content, extract sections, and save to JSON."""
    driver = setup_driver(headless=False)
    FILES_DIR.mkdir(parents=True, exist_ok=True)

    try:
        for index, link in enumerate(links[start_index:], start_index):
            full_url = BASE_URL + link
            try:
                soup = fetch_page(driver, full_url)
                article_tag = soup.find("article")
                if not article_tag:
                    logging.error(f"No <article> found at {full_url}")
                    continue

                # Extract headings and convert to text
                titles = [tag.get_text() for tag in article_tag.find_all(["h1", "h2", "h3"])]
                sections = create_page_sections(titles, str(article_tag))

                payload = {"url": full_url, "sections": sections}
                file_path = FILES_DIR / filename_from_url(full_url, ".json")
                with open(file_path, "w", encoding="utf-8") as outfile:
                    json.dump(payload, outfile, ensure_ascii=False, indent=2)

                logging.info(f"Saved scraped data to {file_path}")
            except Exception as e:
                logging.exception(f"Error processing {full_url}: {e}")
            finally:
                set_last_index(index)
    finally:
        driver.quit()
        logging.info("WebDriver session closed.")


def main() -> None:
    """Main entry point for the scraper script."""
    setup_logging()
    links = get_links()
    last_index = get_last_index()
    total = len(links)

    logging.info(f"Starting scrape: {last_index}/{total} links already processed.")
    process_links(links, last_index)
    logging.info("Scraping completed.")


if __name__ == "__main__":
    main()
