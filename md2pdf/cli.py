"""Core functionality for converting Markdown to PDF."""

import click
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


@click.command()
@click.argument("input_filename", type=click.Path(exists=True, dir_okay=False))
@click.argument("output_filename", type=click.Path(writable=True, dir_okay=False))
def cli(input_filename, output_filename):
    """Convert a Markdown file to a PDF."""
    try:
        convert_md_to_pdf(input_filename, output_filename)
        click.secho(f"✅ Converted {input_filename} → {output_filename}", fg="green")
    except Exception as e:
        click.secho(f"❌ Error: {e}", fg="red")


if __name__ == "__main__":
    cli()
