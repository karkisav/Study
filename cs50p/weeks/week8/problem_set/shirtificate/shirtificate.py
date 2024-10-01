from fpdf import FPDF

class PDF(FPDF):
    def header(self):
        self.set_font("Helvetica", "B", size=45)
        self.cell(0, 60, "CS50 Shirtificate", align="C")
    
    def create_shirtificate(self, name):
        self.add_page()

        self.set_auto_page_break(auto=False, margin=0)

        self.image("shirtificate.png", x="C", y=70)

        self.set_font("helvetica", "B", 30)
        self.set_text_color(255, 255, 255)

        self.set_xy(x=(self.w - self.get_string_width(f"{name} took CS50")) / 2, y=140)
        self.cell(0, 10, f"{name} took CS50", align="C")
        self.output("shirtificate.pdf")

def main():
    name = input("Name: ")

    pdf = PDF(orientation="P", format="A4")

    pdf.create_shirtificate(name)

if __name__ == "__main__":
    main()
