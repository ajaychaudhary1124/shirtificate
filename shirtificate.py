from fpdf import FPDF

class Pdf(FPDF):
    def __init__(self, name=None):
        # Initialize the FPDF object
        self._pdf = FPDF()
        # Add a new page to the PDF
        self._pdf.add_page()
        # Set font for the title
        self._pdf.set_font("helvetica", "B", 40)
        
        # Add title to the PDF
        self._pdf.cell(0, 50, "Wiley Edge Shirtificate", new_x="LMARGIN", new_y="NEXT", align='C')
        
        # Add image to the PDF
        self._pdf.image("shirtificate.png", w=self._pdf.epw)
        
        # Set font for the name text
        self._pdf.set_font("helvetica", "", 25)
        # Set text color to white
        self._pdf.set_text_color(255, 255, 255)
        # Add the name to the PDF
        self._pdf.cell(0, -240, f"{name} took Wiley", border=1, align="C")
    
    # Method to output the PDF to a file
    def output(self, fname):
        self._pdf.output(fname)

# Get the name from user input
name = input("Name: ")
# Create a Pdf object with the provided name
pdf = Pdf(name)
# Output the PDF to a file
pdf.output("shirtificate.pdf")
