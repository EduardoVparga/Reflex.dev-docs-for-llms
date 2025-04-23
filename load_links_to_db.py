# load_links_to_db.py
from pathlib import Path
from utils import set_links


LINKS_FILE_PATH = Path("links.txt")

if LINKS_FILE_PATH.exists():
    links = LINKS_FILE_PATH.read_text(encoding="utf-8").splitlines()
    set_links(links)
    print(f"Loaded {len(links)} links into the database.")
else:
    print(f"Error: {LINKS_FILE_PATH} not found.")