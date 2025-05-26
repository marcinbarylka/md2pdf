# md2pdf

**md2pdf** is a lightweight Python CLI tool for converting Markdown files to PDF using `WeasyPrint`. It includes basic CSS styling and is easy to use thanks to the `click` library.

## ✨ Features

* 📄 Convert `.md` files to `.pdf`
* 🌜 Built-in CSS styling (customizable)
* ⚡ Fast and lightweight – runs in seconds
* 🖥️ User-friendly command-line interface

## 🔧 Installation

### Local development install

```bash
git clone https://github.com/yourusername/md2pdf.git
cd md2pdf
pip install -e .
```

> *Requires Python 3.9+.*

## 🚀 Usage

```bash
md2pdf input.md output.pdf
```

Example:

```bash
md2pdf README.md README.pdf
```

## 🧪 Requirements

* Python 3.9+
* [WeasyPrint](https://weasyprint.org/) (installed via pip, but may require system dependencies – see below)

### System dependencies for WeasyPrint

#### On Ubuntu / Debian:

```bash
sudo apt install libpangocairo-1.0-0 libpangoft2-1.0-0 libgdk-pixbuf2.0-0 libffi-dev libcairo2
```

#### On macOS:

```bash
brew install cairo pango gdk-pixbuf libffi
```

## 📁 Project Structure

```
md2pdf/
├── md2pdf/
│   └── __init__.py
│   └── cli.py
├── pyproject.toml
└── README.md
```

## 📌 Roadmap / TODO

* [ ] Support for external CSS (`--style`)
* [ ] Batch folder conversion
* [ ] PDF metadata support
* [ ] Custom HTML templates

## 👨‍💻 Author

Created by \[Your Name].

## 🛡 License

MIT License
