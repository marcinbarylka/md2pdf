import os
import tempfile

import pytest
from md2pdf import cli


@pytest.fixture
def sample_markdown():
    return "# Hello\n\nThis is a **test**."


def test_load_md(tmp_path, sample_markdown):
    md_file = tmp_path / "test.md"
    md_file.write_text(sample_markdown, encoding="utf-8")

    content = cli.load_md(str(md_file))
    assert content == sample_markdown


def test_apply_styles(sample_markdown):
    html = cli.apply_styles("<h1>Hello</h1><p>This is a <strong>test</strong>.</p>")
    assert "<style>" in html
    assert "<body>" in html
    assert "font-family" in html


def test_save_pdf_creates_file(tmp_path):
    html = "<html><body><h1>Hello PDF</h1></body></html>"
    output_file = tmp_path / "output.pdf"

    cli.save_pdf(html, str(output_file))
    assert output_file.exists()
    assert output_file.stat().st_size > 0


def test_convert_md_to_pdf(tmp_path, sample_markdown):
    input_file = tmp_path / "input.md"
    output_file = tmp_path / "output.pdf"
    input_file.write_text(sample_markdown, encoding="utf-8")

    cli.convert_md_to_pdf(str(input_file), str(output_file))
    assert output_file.exists()
    assert output_file.stat().st_size > 0
