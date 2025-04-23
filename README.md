# Reflex Docs Scraper & Markdown Converter

This project provides a set of Python scripts to scrape documentation pages from `reflex.dev`, process the HTML content, and convert it into Markdown format using a local LLM via Ollama.

## Project Structure
Reflex.dev-docs-for-llms/
├── documents/                 # Output: Generated Markdown files
├── json_html/                 # Intermediate: JSON files with scraped HTML sections
├── extract_content_to_markdown.py
├── extract_links.py
├── links.txt                  # Output: List of scraped documentation links
├── load_links_to_db.py        # Helper script: Loads links.txt into the database
├── scrap_pages.py
└── utils.py

## Overview

The process involves three main steps, orchestrated by separate scripts:

1.  **Link Extraction (`extract_links.py`):** Scans initial seed URLs on `reflex.dev` to discover internal documentation links (`/docs/...`). It handles dynamic content by clicking accordion buttons before parsing. The discovered links are saved to `links.txt`.
2.  **Link Loading & Data Preparation (`load_links_to_db.py`):**  This *helper* script reads the links from `links.txt` and loads them into a database for use by `scrap_pages.py`. This script is crucial as the link extraction only outputs a text file.
3.  **HTML Content Scraping (`scrap_pages.py`):** Reads the links from the database, navigates to each page using Selenium, waits for dynamic content and the main `<article>` tag, scrolls to trigger lazy-loading, and extracts the HTML content within the `<article>`. It then splits this HTML into sections based on `<h1>`, `<h2>`, and `<h3>` tags and saves the URL and sectioned HTML data into individual JSON files in the `json_html/` directory. Progress is tracked to allow resuming.
4.  **Markdown Conversion (`extract_content_to_markdown.py`):** Reads the JSON files generated in the previous step. For each HTML section, it uses a configured Ollama model to convert the HTML to Markdown according to specific rules (e.g., preserving code blocks, converting tables to lists, omitting images). The resulting Markdown sections for each page are combined and saved as `.md` files in the `documents/` directory. Progress is tracked similarly to allow resuming.

A utility script (`utils.py`) provides shared functions for database interaction (using `shelve` for progress tracking), filename generation, section splitting, and file export.

## Features

*   **Automated Link Discovery:** Finds relevant documentation links starting from seed URLs.
*   **Dynamic Content Handling:** Uses Selenium to interact with JavaScript elements (accordions) and handle lazy-loaded content via scrolling.
*   **Targeted Content Extraction:** Focuses on the main `<article>` content of each page.
*   **HTML Sectioning:** Splits scraped HTML into logical chunks based on headings (H1, H2, H3).
*   **LLM-Powered Conversion:** Leverages a local Ollama model for intelligent HTML-to-Markdown conversion.
*   **Custom Conversion Rules:** Specific instructions are given to the LLM via the prompt (e.g., ignore metadata, omit images, handle tables as lists).
*   **Resumable Processing:** Uses a simple database (`shelve`) to track progress for scraping and conversion, allowing scripts to be stopped and restarted without losing work.
*   **Structured Output:** Organizes scraped HTML sections into JSON files and final output into Markdown files.

## Prerequisites

*   **Python 3.12**
*   **Pip** (Python package installer)
*   **Mozilla Firefox**
*   **Geckodriver:** Download the executable compatible with your Firefox version and OS from [mozilla/geckodriver/releases](https://github.com/mozilla/geckodriver/releases). Place it in the project's root directory (next to `extract_links.py`, `load_links_to_db.py`, etc.) or update the `DRIVER_PATH` constant in `extract_links.py` and `scrap_pages.py`.
*   **Ollama:** A running instance of Ollama. See [Ollama website](https://ollama.com/) for installation instructions.
*   **Ollama Model:** The specific model used for conversion must be pulled. By default, this is `qwen2.5:7b-instruct-q6_K`. You can pull it using:
    ```bash
    ollama pull qwen2.5:7b-instruct-q6_K
    ```
    If you use a different model, update the `MODEL` constant in `extract_content_to_markdown.py`.

## Installation

1.  **Clone the repository:**
    ```bash
    git clone git@github.com:EduardoVparga/Reflex.dev-docs-for-llms.git
    cd Reflex.dev-docs-for-llms
    ```
2.  **Create a virtual environment (recommended):**
    ```bash
    python -m venv venv
    source venv/bin/activate # On Windows use `venv\Scripts\activate`
    ```
3.  **Install required Python packages:** Create a `requirements.txt` file with the following content:
    ```txt
    selenium
    beautifulsoup4
    ollama
    ```
    Then install them:
    ```bash
    pip install -r requirements.txt
    ```
4.  **Place `geckodriver`** in the project root or update paths in the scripts.

## Usage

The scripts are designed to be run in sequence. Ensure Ollama is running before starting step 4.

1.  **Extract Initial Links:**
    ```bash
    python extract_links.py
    ```
    This will create `links.txt` containing the discovered documentation URLs and `scraper.log` for logging.

2.  **Load Links into Database:**
    *   Run the helper script:
    ```bash
    python load_links_to_db.py
    ```
    This reads links from `links.txt` and populates the database.  *This is a critical step.*

3.  **Scrape HTML Content:**
    ```bash
    python scrap_pages.py
    ```
    This script will:
    *   Create the `json_html/` directory if it doesn't exist.
    *   Read links from the database (via `utils.get_links()`).
    *   Check the last processed index from `db/progress.db` (created in `db/` directory).
    *   Iterate through the links, scrape content, and save JSON files to `json_html/`.
    *   Update the `last_index` in `db/progress.db` after each file.
    *   You can stop this script (Ctrl+C) and restart it; it will resume from where it left off. Logging goes to stdout.

4.  **Convert HTML to Markdown:**
    *   Ensure your Ollama instance is running and the required model is available.
    ```bash
    python extract_content_to_markdown.py
    ```
    This script will:
    *   Create the `documents/` directory if it doesn't exist.
    *   Reset the `last_index` in the database to 0 (as it processes files based on the *JSON file* index, not the link index).
    *   Read JSON files from `json_html/`.
    *   Check the last processed *file* index from `db/progress.db`.
    *   For each file, send HTML sections to Ollama for conversion.
    *   Save the resulting Markdown to `.md` files in `documents/`.
    *   Update the `last_index` in `db/progress.db` after each file.
    *   You can stop this script (Ctrl+C) and restart it; it will resume processing the JSON files. Logging goes to stdout.

## Configuration

Key parameters can be adjusted directly in the scripts:

*   **`extract_links.py`:**
    *   `URLS_TO_SCRAPE`: List of starting URLs for link discovery.
    *   `CHEVRON_BUTTON_XPATH`: XPath for accordion buttons (may need adjustment if the site structure changes).
    *   `OUTPUT_FILE`: Name of the file to save discovered links (`links.txt`).
    *   `DRIVER_PATH`: Path to the geckodriver executable.
    *   `LOG_FILE`: Name for the log file generated by this script.
*   **`scrap_pages.py`:**
    *   `BASE_URL`: Base URL for constructing full links (`https://reflex.dev`).
    *   `FILES_DIR`: Directory to save intermediate JSON files (`./json_html`).
    *   `DRIVER_PATH`: Path to the geckodriver executable.
    *   `PAGE_LOAD_TIMEOUT`, `ELEMENT_LOAD_TIMEOUT`: Timeouts for Selenium waits.
*   **`extract_content_to_markdown.py`:**
    *   `OLLAMA_URL`: URL of your running Ollama instance (`http://localhost:11434`).
    *   `MODEL`: The Ollama model name to use for conversion.
    *   `FILES_DIR`: Directory containing the JSON files (`./json_html`).
    *   `PROMPT_TEMPLATE`: The prompt sent to the LLM, containing conversion rules.
*   **`utils.py`:**
    *   `DB_FILE`: Path to the `shelve` database file (`./db/progress.db`).
    *   `OUTPUT_DIR` (in `export_to_markdown`): Default directory for final Markdown files (`./documents`).

## Output Files

*   `links.txt`: List of discovered documentation links (relative URLs).
*   `scraper.log`: Log file from `extract_links.py`.
*   `db/progress.db*`: Database files created by `shelve` to store progress (`last_index`) and the list of links (`links`).
*   `json_html/*.json`: Intermediate files, each containing the URL and sectioned HTML content of a scraped page.
*   `documents/*.md`: Final Markdown files generated from the HTML content.

## Contributing

Contributions are welcome! Please feel free to submit issues or pull requests.
