"""Core functionality for converting Markdown to PDF."""

import argparse

from markdown import markdown
from weasyprint import HTML


def load_md(filename: str) -> str:
    """Load a markdown file and return its content."""
    with open(filename, "r", encoding="utf-8") as file:
        return file.read()


def apply_styles(html_content: str) -> str:
    """Apply custom styles to the HTML content."""
    styles = """
    <style>
        body { font-family: Arial, sans-serif; line-height: 1.6; }
        h1, h2, h3 { color: #333; }
        p { margin-bottom: 1em; }
    </style>
    """
    return f"<html><head>{styles}</head><body>{html_content}</body></html>"


def save_pdf(content: str, output_filename: str) -> None:
    """Save the content to a PDF file."""
    HTML(string=content).write_pdf(output_filename)


def convert_md_to_pdf(input_filename: str, output_filename: str) -> None:
    """Convert a markdown file to a PDF file."""
    md_content = load_md(input_filename)
    html_content = markdown(md_content)
    html_content = apply_styles(html_content)
    save_pdf(html_content, output_filename)


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Convert Markdown files to PDF.")
    parser.add_argument("input", help="Input markdown file")
    parser.add_argument("output", help="Output PDF file")

    args = parser.parse_args()

    convert_md_to_pdf(args.input, args.output)
    print(f"Converted {args.input} to {args.output}")
