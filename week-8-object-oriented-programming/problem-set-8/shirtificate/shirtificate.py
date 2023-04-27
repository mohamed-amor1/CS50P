from fpdf import FPDF

# Create a new PDF object with portrait orientation and A4 format
pdf = FPDF(orientation="portrait", format="A4")

# Add a new page to the PDF
pdf.add_page()

# Add an image to the page at the center, with a Y position of 70 and a width of 190
pdf.image("shirtificate.png", x="C", y=70, w=190)

# Set the font to Helvetica with a size of 48, and add a centered text cell with a height of 57 and no borders
pdf.set_font("helvetica", size=48)
pdf.cell(border=0, txt="CS50 Shirtificate", align="C", w=0, h=57)

# Set the font to Helvetica with a size of 24, set the text color to white, and define the text to be displayed
pdf.set_font("helvetica", size=24)
pdf.set_text_color(r=255, g=255, b=255)
text = "Mohamed Amor took CS50"

# Calculate the cell width based on the width of the text plus some padding, and calculate the X position to center the cell
cell_width = pdf.get_string_width(text) + 6
page_width = pdf.w
x_pos = (page_width - cell_width) / 2

# Set the X and Y positions to center the cell, define the width and height of the cell, and add the text with center alignment
pdf.set_xy(x_pos, pdf.y)
pdf.cell(w=cell_width, h=250, txt=text, align="C")

# Output the PDF to a file named "shirtificate.pdf"
pdf.output("shirtificate.pdf")
