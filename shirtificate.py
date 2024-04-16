from fpdf import FPDF


class Pdf(FPDF):
    def __init__(self, name=None):
        self._pdf = FPDF()
        self._pdf.add_page()
        self._pdf.set_font("helvetica", "B", 40)

        self._pdf.cell(0,50, "CS50 Shirtificate", new_x="LMARGIN", new_y="NEXT", align='C')
        self._pdf.image("shirtificate.png",  w=self._pdf.epw)
        self._pdf.set_font("helvetica","", 25)
        self._pdf.set_text_color(255,255,255)
        self._pdf.cell(0,-240,f"{name} took CS50" , border=1, align="C")

    def output(self, fname):
        self._pdf.output(fname)

name = input("Name: ")
pdf = Pdf(name)
pdf.output("shirtificate.pdf")
