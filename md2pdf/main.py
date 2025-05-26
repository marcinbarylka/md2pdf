if __name__ == "__main__":
    from md2pdf.document import Document

    doc = Document("example.md")
    doc.read()
    print(doc.content)
