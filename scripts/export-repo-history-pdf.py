#!/usr/bin/env python3
from reportlab.lib.pagesizes import letter
from reportlab.pdfgen import canvas
from reportlab.lib import colors
from pathlib import Path
import os

def generate_pdf():
    root = Path(__file__).resolve().parent.parent
    md_file = root / 'docs' / 'REPO_HISTORY.md'
    pdf_file = root / 'docs' / 'REPO_HISTORY.pdf'

    if not md_file.exists():
        print("Error: REPO_HISTORY.md not found. Run export-repo-history.py first.")
        return

    c = canvas.Canvas(str(pdf_file), pagesize=letter)
    width, height = letter

    content = md_file.read_text(encoding='utf-8', errors='ignore')
    lines = content.splitlines()

    y = height - 50
    margin = 50
    font_size = 8
    line_height = 10

    c.setFont("Helvetica-Bold", 14)
    c.drawString(margin, y, "Dot_Env Repository History")
    y -= 30

    c.setFont("Courier", font_size)

    for line in lines:
        if y < 50:
            c.showPage()
            c.setFont("Courier", font_size)
            y = height - 50

        # Simple wrapping
        text = line.replace('\t', '    ')
        while len(text) > 100:
            c.drawString(margin, y, text[:100])
            y -= line_height
            text = text[100:]
            if y < 50:
                c.showPage()
                c.setFont("Courier", font_size)
                y = height - 50

        c.drawString(margin, y, text)
        y -= line_height

    c.save()
    print(f"pdf created at {pdf_file}")

if __name__ == "__main__":
    generate_pdf()
