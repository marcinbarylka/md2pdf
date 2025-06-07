"""Core functionality for converting Markdown to PDF."""

import click
from markdown import markdown
from weasyprint import HTML
import os


def load_md(filename: str) -> str:
    """Load a markdown file and return its content."""
    with open(filename, "r", encoding="utf-8") as file:
        return file.read()


def apply_styles(html_content: str) -> str:
    """Apply custom styles to the HTML content."""
    styles = """
    <style>
        body { font-family: Arial, sans-serif; line-height: 1.6; font-size: 14px; }
        h1, h2, h3 { color: #333; }
        p { margin-bottom: 1em; }
        .text-right {
            text-align: right;
        }
        .text-center {
            text-align: center;
        }
        .text-justify {
            text-align: justify;
        }
        .indent-right {
            margin-left: 50%;
        }
        .indent-right-60 {
            margin-left: 60%;
        }
        .indent-right-40 {
            margin-left: 40%;
        }
        table {
            border-collapse: collapse;
            width: 100%;
            margin: 1em 0;
        }
        th, td {
            border: 1px solid #ddd;
            padding: 8px;
        }
        th {
            background-color: #f5f5f5;
        }
        tr:nth-child(even) {
            background-color: #f9f9f9;
        }
        td[align="right"], th[align="right"] {
            text-align: right;
        }
        td[align="center"], th[align="center"] {
            text-align: center;
        }
        td[align="left"], th[align="left"] {
            text-align: left;
        }
    </style>
    """
    return f"<html><head>{styles}</head><body>{html_content}</body></html>"


def save_pdf(content: str, output_filename: str) -> None:
    """Save the content to a PDF file."""
    HTML(string=content).write_pdf(output_filename)


def convert_md_to_pdf(input_filename: str, output_filename: str) -> None:
    """Convert a markdown file to a PDF file."""
    md_content = load_md(input_filename)
    html_content = markdown(md_content, extensions=['tables', 'attr_list', 'nl2br'])
    html_content = apply_styles(html_content)
    save_pdf(html_content, output_filename)


@click.command()
@click.argument("input_filename", type=click.Path(exists=True, dir_okay=False))
@click.argument("output_filename", type=click.Path(writable=True, dir_okay=False), required=False)
def cli(input_filename, output_filename=None):
    """Convert a Markdown file to a PDF.

    If OUTPUT_FILENAME is not provided, it will be generated from INPUT_FILENAME
    by replacing the .md extension with .pdf
    """
    try:
        if output_filename is None:
            base, ext = os.path.splitext(input_filename)
            output_filename = f"{base}.pdf"

        convert_md_to_pdf(input_filename, output_filename)
        click.secho(f"✅ Converted {input_filename} → {output_filename}", fg="green")
    except Exception as e:
        click.secho(f"❌ Error: {e}", fg="red")


if __name__ == "__main__":
    cli()
