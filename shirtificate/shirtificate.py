from fpdf import FPDF

def main():
    name = input("enter your name: ")
    print(shirtificate(name))



def shirtificate(n):
    pdf = FPDF()
    pdf.add_page()
    pdf.image("/workspaces/193590090/shirtificate/shirtificate.png", x=20, y=60)

    pdf = FPDF(orientation="P", unit="mm", format="A4")
    pdf.set_font("helvetica", style="B", size=16)
    pdf.cell(40, 10, "{input}")

    pdf.set_font("Times", size=12)
    for i in range(1, 41):
        pdf.cell(0, 10, f"CS50 Shirtificate {i}", new_x="LMARGIN", new_y="NEXT")
    pdf.output("shirtificate.pdf")



if __name__ == "__main__":
    main()

