from fpdf import FPDF

def main():
    name = input("enter your name: ")
    shirtificate(name)



def shirtificate(n):
    pdf = FPDF(orientation="P", unit="mm", format="A4")
    pdf.add_page()
    pdf.image("shirtificate.png", x=(210 - pdf.w), y=60)

    pdf.set_font("helvetica", style="B", size=30)
    pdf.set_text_color(255, 255, 255)
    pdf.cell(0, 200, f"{name} took CS50", align="C")
    pdf.output("shirtificate.pdf")


if __name__ == "__main__":
    main()

