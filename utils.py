import shelve
from pathlib import Path
import logging
from typing import Any, List
import re

# Configure logging
logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s | %(levelname)s | %(name)s | %(message)s",
    datefmt="%Y-%m-%d %H:%M:%S",
)
logger = logging.getLogger(__name__)

DB_DIR = Path("./db")
DB_FILE = DB_DIR / "progress.db"


class DBManager:
    """Simple manager for shelve-based persistent storage."""

    def __init__(self, db_path: Path = DB_FILE):
        self.db_path = db_path
        DB_DIR.mkdir(parents=True, exist_ok=True)

    def read(self, key: str, default: Any = None) -> Any:
        logger.debug(f"Reading key '{key}' from database.")
        try:
            with shelve.open(str(self.db_path)) as db:
                value = db.get(key, default)
            logger.info(f"Read '{key}': {value!r}")
            return value
        except Exception as e:
            logger.error(f"Error reading '{key}': {e}")
            return default

    def save(self, key: str, value: Any) -> None:
        logger.debug(f"Saving key '{key}' with value {value!r}")
        try:
            with shelve.open(str(self.db_path)) as db:
                db[key] = value
            logger.info(f"Saved '{key}'.")
        except Exception as e:
            logger.error(f"Error saving '{key}': {e}")


db_manager = DBManager()


def get_last_index() -> int:
    """Retrieve the last processed index (default 0)."""
    return db_manager.read("last_index", default=0)


def set_last_index(index: int) -> None:
    """Store the last processed index."""
    db_manager.save("last_index", index)


def get_links() -> List[str]:
    """Retrieve the saved links (default empty list)."""
    return db_manager.read("links", default=[])


def set_links(links: List[str]) -> None:
    """Store the list of links."""
    db_manager.save("links", links)


def create_page_sections(titles: List[str], article: str) -> List[str]:
    """
    Split an article into sections based on provided titles.
    Each section includes its heading and text up to the next heading.
    """
    logger.debug("Creating page sections.")
    sections: List[str] = []
    for i, title in enumerate(titles):
        start = article.find(title)
        if start == -1:
            logger.warning(f"Title '{title}' not found; skipping.")
            continue
        end = article.find(titles[i + 1], start) if i + 1 < len(titles) else len(article)
        section = article[start:end].strip()
        logger.debug(f"Section {i} starts with: {section[:30]!r}")
        sections.append(section)
    logger.info(f"Created {len(sections)} sections.")
    return sections


def filename_from_url(url: str, extension: str = ".md") -> str:
    """
    Convert a URL into a filesystem‑safe filename.

    Steps:
      1. Strip protocol.
      2. Strip trailing slash.
      3. Replace invalid filename characters with '_'.
      4. Append the given extension.
    """
    logger.debug(f"Generating filename from URL: {url}")
    url_no_protocol = re.sub(r"^https?://", "", url).rstrip("/")
    base = re.sub(r"[^a-zA-Z0-9._-]", "_", url_no_protocol)
    filename = f"{base}{extension}"
    logger.info(f"Generated filename: {filename}")
    return filename


def export_to_markdown(
    content: str,
    filename: str = "output.md",
    output_dir: Path = Path("./documents"),
) -> None:
    """
    Write the given content to a Markdown file in the specified directory.
    """
    logger.debug(f"Exporting content to '{filename}' in '{output_dir}'.")
    output_dir.mkdir(parents=True, exist_ok=True)
    file_path = output_dir / filename
    try:
        file_path.write_text(content, encoding="utf-8")
        logger.info(f"Successfully exported Markdown to: {file_path}")
    except IOError as e:
        logger.error(f"Failed to write file {file_path}: {e}")
        raise
