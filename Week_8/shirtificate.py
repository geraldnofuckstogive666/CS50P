#https://cs50.harvard.edu/python/psets/8/shirtificate/

from fpdf import FPDF

class PDF(FPDF):
    def header(self):
        self.set_font("helvetica", style="B", size=32)
        self.cell(0, 10, "CS50 Shirtificate", border=0, align="C")
        self.ln(10)


pdf = PDF()
pdf.add_page()
pdf.set_auto_page_break(auto=False)
page_width = 210
image_width = 180
image_y = 50
x = (page_width - image_width) / 2
pdf.image("shirtificate.png", x=x, y=image_y, w=image_width)


def get_name():
    user_input = input("Name: ").strip().title()
    return f"{user_input} took CS50"

text = get_name()
pdf.set_text_color(255, 255, 255)

text_width = pdf.get_string_width(text)
text_x = x + (image_width - text_width) / 2
text_y = image_y + image_width / 2 - 20
pdf.text(text_x, text_y, text)


pdf.output("shirtificate.pdf")