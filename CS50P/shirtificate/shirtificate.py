from lib2to3.pytree import convert
from fpdf import FPDF

class PDF(FPDF):
    def __init__(self):
        super().__init__(orientation='portrait', format='A4')

    def header(self):
        self.set_font("helvetica", size=35)
        # Moving cursor to the right:
        self.cell(80)
        # Printing title:
        self.cell(30, 15, "CS50 Shirtificate",  align="C")


    def page_front(self, title):
        self.add_page()
        self.image("shirtificate.png", h = self.eph, w = self.epw,  x= 8, y = 45)
        self.add_shape(title)


    def add_shape(self, title):
        self.set_line_width(2)
        self.set_draw_color(r=255, g=255, b=255)
        self.set_fill_color(r=106, g=17, b=52)
        self.ellipse(x = 49, y = 100, w = 1.8 * self.epw/3, h=50, style="FD")
        self.add_title(title)

    def add_title(self, title):
        self.set_font_size(25)
        self.set_text_color(r=255, g=255, b=255)
        self.cell(-60)
        self.cell(95, 235, txt=title, align="C")

def main():
    name = input("Name: ")
    create(name)

def create(name):
    title = name + " took CS50"
    pdf = PDF()
    pdf.page_front(title)
    pdf.output("shirtificate.pdf")


if __name__ == "__main__":
    main()