import json
import logging
import time
from pathlib import Path
from typing import List

import ollama

from utils import get_last_index, set_last_index, filename_from_url, export_to_markdown

# Constants
OLLAMA_URL = "http://localhost:11434"
MODEL = "qwen2.5:7b-instruct-q6_K"
FILES_DIR = Path("./json_html")

PROMPT_TEMPLATE = """I want you to convert the following HTML code into Markdown format. Please follow these rules:

- Ignore any metadata such as <script>, <style>, <meta> tags or HTML comments.
- Do not include content from scripts or styles.
- Preserve the structure of headings, paragraphs, lists using Markdown syntax.
- Avoid any styling tags or attributes that are not relevant in Markdown.
- HTML usage in the response is strictly forbidden.
- Avoid unnecessary introductions. Provide the response directly.
- Omit images, jpg, svg, png, etc. It is forbidden to convert image references to Markdown.
- Preserve python code examples.
- Transform tables into lists. The character "|" is not a column separator. Use markdown table syntax is forbidden.
- Dont use tables in markdown.

---

I will now provide the HTML. Return **only** the content in Markdown format:

{html}
"""

logger = logging.getLogger(__name__)


def setup_logging() -> None:
    """Configure root logger for the script."""
    logging.basicConfig(
        level=logging.INFO,
        format="%(asctime)s [%(levelname)s] %(message)s",
        datefmt="%Y-%m-%d %H:%M:%S",
    )


def load_json_files(directory: Path) -> List[Path]:
    """Return a sorted list of JSON file paths in the given directory."""
    return sorted(directory.glob("*.json"))


def process_file(client: ollama.Client, file_path: Path, file_index: int) -> None:
    """Process a single JSON file: convert sections to Markdown and export."""
    logger.info("Processing file %d: %s", file_index, file_path.name)
    try:
        data = json.loads(file_path.read_text(encoding="utf-8"))
        url = data.get("url", "")
        sections = data.get("sections", [])
        logger.info("Found %d sections in %s", len(sections), file_path.name)

        markdown_sections: List[str] = []
        for sec_num, section in enumerate(sections, start=1):
            start_time = time.perf_counter()
            logger.info("Converting section %d/%d", sec_num, len(sections))

            response = client.generate(
                model=MODEL,
                prompt=PROMPT_TEMPLATE.format(html=section),
                options={
                    "num_ctx": 12048,
                    "temperature": 0.7,
                },
            )
            md = response.get("response", "").strip()
            markdown_sections.append(md)

            elapsed = time.perf_counter() - start_time
            logger.info("Section %d processed in %.3f seconds", sec_num, elapsed)

        output_content = "\n\n".join(markdown_sections)
        output_filename = filename_from_url(url)
        export_to_markdown(output_content, output_filename)

        set_last_index(file_index + 1)
        logger.info(
            "Exported Markdown to %s and updated last index to %d",
            output_filename,
            file_index + 1,
        )

    except Exception as e:
        logger.error(
            "Error processing %s: %s", file_path.name, e, exc_info=True
        )


def main() -> None:
    """Main entry point of the script."""
    setup_logging()
    logger.info("Starting HTML → Markdown conversion script")

    client = ollama.Client(host=OLLAMA_URL)
    json_files = load_json_files(FILES_DIR)
    last_index = get_last_index()
    total_files = len(json_files)
    logger.info("Total files: %d; resuming from index: %d", total_files, last_index)

    for idx, file_path in enumerate(json_files):
        if idx < last_index:
            continue
        process_file(client, file_path, idx)

    logger.info("Processing complete.")


if __name__ == "__main__":
    main()
