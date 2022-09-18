from fpdf import FPDF


def main():
    name = input("Enter your name: ")
    createPDF(name)
    print("Success!!")


def createPDF(myname):
    fpdf = FPDF()

    #add a blank page
    fpdf.add_page()

    #add txt
    fpdf.set_font("helvetica", "", 46)
    fpdf.cell(w=0, h=50, txt="CS50 Shirtificate", align="C")
    fpdf.ln(50)

    #add image
    fpdf.image("shirtificate.png", w = 190)

    #add name on shirt
    fpdf.set_font("helvetica", "", 25)
    fpdf.set_text_color(255, 255, 255)
    fpdf.cell(w=0, h=-250, txt=f"{myname} took CS50", align="C")

    #save document
    fpdf.output("output.pdf")

if __name__ == "__main__":
    main()
