# encoding:utf-8
from pdf_prep import PDF
import locale
import webbrowser as wb
from datetime import datetime
import time
from tkinter import messagebox



def printed(data,au):
    pdf = PDF(orientation="landscape")
    pdf.add_page()

    pdf.add_font("DejaVu", "", "fonts/DejaVuSans.ttf")
    pdf.add_font("DejaVu", "B", "fonts/DejaVuSans-Bold.ttf")
    pdf.add_font("DejaVu", "I", "fonts/DejaVuSans-Oblique.ttf")
    pdf.add_font("DejaVu", "BI", "fonts/DejaVuSans-BoldOblique.ttf")

    pdf.set_font("DejaVu", size=20)
    pdf.set_author("Cashpad V1.5.3")
    pdf.cell(0, 10, "KASA DÖKÜMÜ", align="C")
    pdf.ln()
    pdf.set_font("DejaVu", size=12)
    pdf.create_table(table_data = data,title=f'Kurum: Sarmal Plus Eğitim Kurumları -> {datetime.now()}', cell_width='even')
    pdf.ln()
    pdf.ln()


    filename = f"reports\\RAPOR{datetime.now().day}{datetime.now().month}{datetime.now().year}.pdf"
    pdf.output(filename)
    #infowin = messagebox.showinfo(title="Evrakları toparlıyoruz.", message="Biz raporu hazırlarken lütfen bekleyiniz.")
    #time.sleep(2)
    wb.open(filename)

