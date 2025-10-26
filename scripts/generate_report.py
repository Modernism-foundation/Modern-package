import os
import datetime
from reportlab.lib.pagesizes import A4
from reportlab.pdfgen import canvas

def generate_pdf(input_md, output_pdf):
    if not os.path.exists(input_md):
        print(f"❌ Template not found: {input_md}")
        return

    with open(input_md, "r", encoding="utf-8") as f:
        lines = f.readlines()

    c = canvas.Canvas(output_pdf, pagesize=A4)
    width, height = A4
    y = height - 50

    c.setFont("Helvetica-Bold", 16)
    c.drawString(50, y, "Modern-package Project Report")
    y -= 30
    c.setFont("Helvetica", 10)
    c.drawString(50, y, f"Generated on {datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
    y -= 40

    c.setFont("Helvetica", 11)
    for line in lines:
        if y < 50:
            c.showPage()
            y = height - 50
        c.drawString(50, y, line.strip())
        y -= 15

    c.save()
    print(f"✅ Report generated: {output_pdf}")

if __name__ == "__main__":
    os.makedirs("docs", exist_ok=True)
    generate_pdf("docs/report_template.md", "docs/report.pdf")
