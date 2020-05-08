from reportlab.lib.enums import TA_JUSTIFY
from reportlab.lib.pagesizes import letter
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer, Image
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.lib.units import inch
import qrcode


class QR_and_PDF:
    def __init__(self, idnumber, name, fathername, designation):
        self.idnumber = idnumber
        self.name = name
        self.fname = fathername
        self.Designation = designation
        self.printpdf()

    def QR_code(self,id,name):
        qrcodename="static/QR_Code/"+str(id)+str(name)+".png"
        qr = qrcode.QRCode(
            version=1,
            border=1,
            box_size=10
        )
        data = "hello world how are you"

        qr.add_data(data)
        qr.make(fit=True)
        img = qr.make_image(fill='black', back_color='white')
        img.save(qrcodename)
        return qrcodename

    def printpdf(self):
        self.filename="static/pdf/"+str(self.idnumber)+str(self.name)+".pdf"

        doc = SimpleDocTemplate(self.filename, pagesize=letter,
                                rightMargin=72, leftMargin=72,
                                topMargin=72, bottomMargin=18)
        Story = []
        logo = self.QR_code(self.idnumber,self.name)

        im = Image(logo, 2 * inch, 2 * inch, hAlign='LEFT')
        Story.append(im)

        styles = getSampleStyleSheet()
        styles.add(ParagraphStyle(name='Justify', alignment=TA_JUSTIFY))
        Story.append(Spacer(1, 20))
        ptext = '<font size=12><b>Id No.</b> : %s</font>' % self.idnumber
        Story.append(Paragraph(ptext, styles["Normal"]))
        Story.append(Spacer(1, 5))

        ptext = '<font size=12><b>name.</b> : %s</font>' % self.name
        Story.append(Paragraph(ptext, styles["Normal"]))
        Story.append(Spacer(1, 5))
        ptext = '<font size=12><b>F Name\'s.</b> : %s</font>' % self.fname
        Story.append(Paragraph(ptext, styles["Normal"]))
        Story.append(Spacer(1, 5))
        ptext = '<font size=12><b>Designation.</b> : %s</font>' % self.Designation
        Story.append(Paragraph(ptext, styles["Normal"]))
        Story.append(Spacer(1, 5))
        doc.build(Story)
        return self.filename

    def __str__(self):
        return self.filename

if __name__ == '__main__':
    p=QR_and_PDF(5,'rahul','sunil','CEO')
    print(p)
