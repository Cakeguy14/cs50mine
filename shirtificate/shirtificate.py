from fpdf import FPDF

pdf = FPDF()
pdf.add_page()
pdf = FPDF(orientation="P", unit="mm", format="A4")
pdf.set_font("helvetica", style="B", size=16)
pdf.cell(40, 10, "CS50 Shirtificate")
pdf.output("tuto1.pdf")

def header():
    pdf = PDF()
    pdf.add_page()
    pdf.set_font("Times", size=12)
    for i in range(1, 41):
        pdf.cell(0, 10, f"CS50 Shirtificate {i}", new_x="LMARGIN", new_y="NEXT")
    pdf.output("shirtificate.pdf")
