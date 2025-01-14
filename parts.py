from tkinter import *
import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
from elements import cbutton
from elements import sort_by_date
from PIL import ImageTk, Image
from datetime import datetime
import sqlite3 as sq
import pdfexport as pex
import matplotlib.pyplot as plt 
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg as fct

def btn_changer(panel):
        for widgets in panel.panel.winfo_children():
            widgets.configure(background = "RoyalBlue1",foreground = "white")

def clear_frame(frame_base):
        for widgets in frame_base.winfo_children():
            widgets.destroy()

def home_page(panel):
    btn_changer(panel)
    clear_frame(panel.base)
    panel.home_page_btn.configure(background="white", foreground="black")
    work_image = Image.open('images/workingon.png')
    work_image = work_image.resize((338,482))
    work_image = ImageTk.PhotoImage(work_image)
    work_label = tk.Label(master=panel.base,background="white",image=work_image)
    work_label.img_reference = work_image
    work_label.pack(fill="both",padx=10,pady=10)
    tk.Label(master=panel.base,background="yellow",text="Henüz tamamlanmadı.\n\t Üzerinde çalışıyoruz...",font=("Calibri",14,"italic")).pack(fill="x")
def printer(au):
    mydb = sq.connect('CDF.db')
    mycursor = mydb.cursor()
    query = f"Select * from payment_base"
    mycursor.execute(query)
    finded = mycursor.fetchall()
    finded = sort_by_date(finded)
    data = [["Tarih", "İşleyen","Tip", "Alan","Açıklama","Tutar (₺)"]]        

    for i in finded:
        data.append([i[1],i[2].capitalize(),i[3].capitalize(),i[4].capitalize(),i[5],i[6]])

    pex.printed(data,au)


def sum_of_case():
    mydb = sq.connect('CDF.db')
    mycursor = mydb.cursor()
    query_gelir = f"Select * from payment_base where type like 'gelir'"
    mycursor.execute(query_gelir)
    finded_gelir = mycursor.fetchall()

    query_gider = f"Select * from payment_base where type like 'gider'"
    mycursor.execute(query_gider)
    finded_gider = mycursor.fetchall()

    total_gelir = 0.0
    for i in finded_gelir:
        total_gelir = total_gelir + float(i[6])

    total_gider = 0.0
    for i in finded_gider:
        total_gider = total_gider + float(i[6])

    mycursor.close()
    mydb.close()

    return [total_gelir, total_gider, total_gelir-total_gider]



def delete_from_tree(tree):
    pass


def case_page(panel):
    btn_changer(panel)
    clear_frame(panel.base)
    panel.case_btn.configure(background="white", foreground="red")

    summary_btn_image = Image.open('images/eye.png')
    summary_btn_image = summary_btn_image.resize((20,20))
    summary_btn_image = ImageTk.PhotoImage(summary_btn_image)

    filter_btn_image = Image.open('images/filter.png')
    filter_btn_image = filter_btn_image.resize((20,20))
    filter_btn_image = ImageTk.PhotoImage(filter_btn_image)     

    printer_btn_image = Image.open('images/printer.png')
    printer_btn_image = printer_btn_image.resize((20,20))
    printer_btn_image = ImageTk.PhotoImage(printer_btn_image)  

    profile_btn_image = Image.open('images/mode-portrait.png')
    profile_btn_image = profile_btn_image.resize((20,20))
    profile_btn_image = ImageTk.PhotoImage(profile_btn_image)  

    cash_btn_image = Image.open('images/sack-dollar.png')
    cash_btn_image = cash_btn_image.resize((20,20))
    cash_btn_image = ImageTk.PhotoImage(cash_btn_image)  

    based = tk.Frame(panel.base, background="white",highlightthickness=0)
    based.pack(fill="both",expand=TRUE,padx=10, pady=10)

    case_page_top_bar = tk.Frame(based,background="white")
    case_page_top_bar.pack(side="top",fill="x",padx=5,pady=5)
    
    summary_btn = tk.Button(master=case_page_top_bar,border=0,relief="flat",image=summary_btn_image,background="white")
    summary_btn.img_reference = summary_btn_image
    summary_btn.pack(side="right",fill="x")

    filter_btn = tk.Button(master=case_page_top_bar,border=0,relief="flat",image=filter_btn_image,background="white")
    filter_btn.img_reference = filter_btn_image
    filter_btn.pack(side="right",fill="x")

    printer_btn = tk.Button(master=case_page_top_bar,border=0,relief="flat",image=printer_btn_image,background="white",command=lambda: printer(panel.au.capitalize()))
    printer_btn.img_reference = printer_btn_image
    printer_btn.pack(side="right",fill="x")

    profile_btn = tk.Button(master=case_page_top_bar,border=0,relief="flat",image=profile_btn_image,background="white")
    profile_btn.img_reference = profile_btn_image
    profile_btn.pack(side="left",fill="x")
    tk.Label(case_page_top_bar,text=f" {panel.au}",font=("Calibri",14,"bold"),background="white").pack(side="left",fill="x")
    tk.Label(case_page_top_bar,text="      ",background="white").pack(side="left",fill="x")


    cash_btn = tk.Button(master=case_page_top_bar,border=0,relief="flat",image=cash_btn_image,background="white")
    cash_btn.img_reference = cash_btn_image
    cash_btn.pack(side="left",fill="x")
    tk.Label(case_page_top_bar,text=f"{sum_of_case()[0]}",foreground="blue",font=("Calibri",14,"bold"),background="white").pack(side="left",fill="x")
    tk.Label(case_page_top_bar,text=f"{sum_of_case()[1]}",foreground="red",font=("Calibri",14,"bold"),background="white").pack(side="left",fill="x")
    tk.Label(case_page_top_bar,text=f"{sum_of_case()[2]}",foreground="green",font=("Calibri",14,"bold"),background="white").pack(side="left",fill="x")


    case_page_poz_frame = tk.Frame(based, background="green",highlightthickness=2, relief="flat")
    case_page_neg_frame = tk.Frame(based, background="red",highlightthickness=2, relief="flat")

    case_page_poz_frame.pack(side="left",fill="both",expand=True,padx=5)
    case_page_neg_frame.pack(side="left",fill="both",expand=True,padx=5)
    
    case_page_poz_frame.pack_propagate(False)
    case_page_neg_frame.pack_propagate(False)

    
    poz_list = Trees(case_page_poz_frame,"gelir", panel.au, panel).create()
    poz_list.pack(fill="both",expand=True)
    neg_list = Trees(case_page_neg_frame,"gider",panel.au, panel).create()
    neg_list.pack(fill="both",expand=True)

    
def take_data(sector,type):
    mydb = sq.connect('CDF.db')
    mycursor = mydb.cursor()
    query = f"Select * from payment_base where {sector} like '{type}'"
    mycursor.execute(query)
    finded = sort_by_date(mycursor.fetchall())

    return finded

def status_page(panel):
    btn_changer(panel)
    clear_frame(panel.base)
    panel.status_btn.configure(background="white", foreground="black")
    
    gelir_base = take_data("type","Gelir")
    gelir_header = []
    gelir_oran = []
    total_gelir = 0
    
    
    gider_base = take_data("type","Gider")
    gider_header = []
    gider_oran = []
    total_gider = 0

    for i in gelir_base:
        total_gelir = total_gelir + float(i[-1])
        if i[4] in gelir_header:
            pass
        else:
            gelir_header.append(i[4])

    for i in gelir_header:
        part_sum = 0
        taken = take_data("status",i)
        for j in taken:
            part_sum = part_sum + float(j[-1])
        gelir_oran.append(part_sum)



    for i in gider_base:
        total_gider = total_gider + float(i[-1])
        if i[4] in gider_header:
            pass
        else:
            gider_header.append(i[4])

    for i in gider_header:
        part_min = 0
        taken = take_data("status",i)
        for j in taken:
            part_min = part_min + float(j[-1])
        gider_oran.append(part_min)


    colors_poz =['#7900FF', '#548CFF', '#93FFD8', '#CFFFDC', '#FFD2A5', '#FFA08B', '#FF6A5C', '#FF3A3A']

    colors_neg = ['#001F54', '#0047AB', '#4682B4', '#87CEEB', '#ADD8E6', '#B0E0E6', '#AFDBF5', '#D1EAF5']

    fig  = plt.figure(1)

    if total_gelir != 0 :
        plt.subplot(131)
        plt.title(f"Toplam Kurum Geliri : {total_gelir}")
        plt.pie(gelir_oran,labels=gelir_header,autopct='%1.1f%%',colors=colors_poz)
        #plt.subplot(222)
        #plt.bar(gelir_header, gelir_oran)
        #plt.xticks(rotation=90)
    else:
        tk.messagebox.showwarning(title="Yetersiz Veri", message="Hesaplama bilgilerinin sunulabilmesi için daha fazla veriye ihtiyacımız var. Lütfen daha fazla veri ekleyin.")
    
    if total_gider != 0 :
        plt.subplot(133)
        plt.title(f"Toplam Kurum Gideri : {total_gider}")
        plt.pie(gider_oran,labels=gider_header,autopct='%1.1f%%',colors=colors_neg)
    else:
        tk.messagebox.showwarning(title="Yetersiz Veri", message="Hesaplama bilgilerinin sunulabilmesi için daha fazla veriye ihtiyacımız var. Lütfen daha fazla veri ekleyin.")
    
    
    plot_floor = fct(fig,master=panel.base)
    plot_floor.get_tk_widget().pack(fill="both",expand=True)
    plt.close('all')



def see_page(panel):
    btn_changer(panel)
    clear_frame(panel.base)
    panel.see_btn.configure(background="white", foreground="black")
    work_image = Image.open('images/workingon.png')
    work_image = work_image.resize((338,482))
    work_image = ImageTk.PhotoImage(work_image)
    work_label = tk.Label(master=panel.base,background="white",image=work_image)
    work_label.img_reference = work_image
    work_label.pack(fill="both",padx=10,pady=10)
    tk.Label(master=panel.base,background="yellow",text="Henüz tamamlanmadı.\n\t Üzerinde çalışıyoruz...",font=("Calibri",14,"italic")).pack(fill="x")
def about_page(panel):
    btn_changer(panel)
    clear_frame(panel.base)
    panel.about_btn.configure(background="white", foreground="black")
    tk.Label(master=panel.base,background="white",text="Uygulama Hakkında",font=("Calibri",14,"bold")).pack(fill="x",pady=50)
    work_image = Image.open('images/resmilogo.png')
    work_image = work_image.resize((int(work_image.width/3),int(work_image.height/3)))
    work_image = ImageTk.PhotoImage(work_image)
    work_label = tk.Label(master=panel.base,background="white",image=work_image)
    work_label.img_reference = work_image
    work_label.pack(fill="both",padx=10,pady=10)
    tk.Label(master=panel.base,background="white",text="Cashpad v1.0B",font=("Calibri",12,"bold")).pack(fill="x")
    tk.Label(master=panel.base,background="white",text="Uygulama Enes YILDIRIM tarafından Nabla Bilişim S. adına tasarlanmıştır.",font=("Calibri",12)).pack(fill="x")
    tk.Label(master=panel.base,background="white",text="Mevcut beta süreci sonuna kadar GNU-Kamu Lisansına sahiptir.",font=("Calibri",12)).pack(fill="x")

    
class Left_Panel:
    def __init__(self,master, base,background,au) -> None:
        self.master = master
        self.background = background
        self.font=("Calibri",12)
        self.base = base
        self.au = au

        self.home_btn_image = Image.open('images/home.png')
        self.home_btn_image = self.home_btn_image.resize((20,20))
        self.home_btn_image = ImageTk.PhotoImage(self.home_btn_image)

        self.case_btn_image = Image.open('images/coins.png')
        self.case_btn_image = self.case_btn_image.resize((20,20))
        self.case_btn_image = ImageTk.PhotoImage(self.case_btn_image)

        self.status_btn_image = Image.open('images/stats.png')
        self.status_btn_image = self.status_btn_image.resize((20,20))
        self.status_btn_image = ImageTk.PhotoImage(self.status_btn_image)


        self.about_btn_image = Image.open('images/question-square.png')
        self.about_btn_image = self.about_btn_image.resize((20,20))
        self.about_btn_image = ImageTk.PhotoImage(self.about_btn_image)

        


    
    def create(self):
        
        self.panel = tk.Frame(self.master,
                              background=self.background,
                              highlightthickness=0)
        
        self.home_page_btn = cbutton(master=self.panel,image=self.home_btn_image,background="RoyalBlue1",command=lambda : home_page(self)).create()
        self.home_page_btn.pack(fill="x", ipadx=10,ipady=10)

        self.case_btn = cbutton(master=self.panel,image=self.case_btn_image,background="RoyalBlue1",command=lambda : case_page(self)).create()
        self.case_btn.pack(fill="x", ipadx=10,ipady=10)

        self.status_btn = cbutton(master=self.panel,image=self.status_btn_image,background="RoyalBlue1",command=lambda : status_page(self)).create()
        self.status_btn.pack(fill="x", ipadx=10,ipady=10)

        #self.see_btn = cbutton(master=self.panel,font=self.font,text="Gözlem",text_color="white",background="RoyalBlue1",command=lambda : see_page(self)).create()
        #self.see_btn.pack(fill="x", ipadx=10,ipady=10)

        self.about_btn = cbutton(master=self.panel,image=self.about_btn_image,background="RoyalBlue1",command=lambda : about_page(self)).create()
        self.about_btn.pack(fill="x", ipadx=10,ipady=10)

        case_page(self)

        return self.panel
    

class Trees:
    def __init__(self,master,type, au, panel) -> None:
        self.panel = panel
        self.master=master
        self.type = type
        self.status = ""
        self.au = au
        self.nowdate = datetime.now()
        self.this_month = str(self.nowdate.month)
        self.this_year =  str(self.nowdate.year)
        self.this_day =   str(self.nowdate.day)
        self.add_btn_image = Image.open('images/squareplus.png')
        self.add_btn_image = self.add_btn_image.resize((20,20))
        self.add_btn_image = ImageTk.PhotoImage(self.add_btn_image)

        self.sub_btn_image = Image.open('images/squareminus.png')
        self.sub_btn_image = self.sub_btn_image.resize((20,20))
        self.sub_btn_image = ImageTk.PhotoImage(self.sub_btn_image)


    


    def save(self):
        def kayit(date, active_user, tip, status, inf, tutar):
            
            mydb = sq.connect('CDF.db')
            mycursor = mydb.cursor()
            if date == "" or tip == "" or inf == "" or tutar == "" or status == "Alan seçin veya yeni alan girin." or status == "" or len(status) < 4:
                messagebox.showerror(title=f"Hatalı veri girişi!", message=f"Lütfen istenilen bilgileri eksiksiz ve uygun formatta doldurunuz!")
                mydb.commit()
            else:
                query = f"insert into payment_base (date, user, type, status, info, payment) values('{date}','{active_user}','{tip}','{status}','{inf}','{tutar}')"
                mycursor.execute(query)
                messagebox.showinfo(title=f"{tip.capitalize()} kaydedildi.", message=f"{date} tarihli {tutar} tutarlı {tip}iniz başarı ile veri tabanına eklendi.")
                mydb.commit()
                mydb.close()
                case_page(self.panel)


        
        if len(self.this_day) == 1:
            self.this_day = "0" + self.this_day
        
        if len(self.this_month) == 1:
            this_month = "0"+this_month
        
        today_date = f"{self.this_day}/{self.this_month}/{self.this_year}"

        if self.type == "gelir":
            backgr = "spring green"
        else:
            backgr = "orange"
        add_frame = tk.Frame(master=self.master,background="white")
        add_frame.place(x=0,y=0,relwidth=1.0,relheight=1.0)
        add_frame_topbar = tk.Frame(master=add_frame,background=backgr)
        add_frame_topbar.pack(side="top",fill="x")

        close_btn_image = Image.open('images/close_button.png')
        close_btn_image = close_btn_image.resize((20,20))
        close_btn_image = ImageTk.PhotoImage(close_btn_image)

        close_frame_btn = tk.Button(master=add_frame_topbar,image=close_btn_image,
                                    relief="flat",background=backgr,command=lambda:add_frame.destroy())
        close_frame_btn.img_reference = close_btn_image
        close_frame_btn.pack(side="right",fill="y")

        tk.Label(master=add_frame_topbar,text=f"  {self.type.capitalize()} Ekle:",background=backgr,font=("Calibri",14,"bold")).pack(side="left",fill="y")

        #-----------------------------------------------------------------------------
        date_frame = tk.Frame(master=add_frame,relief="flat",background="white")
        date_frame.pack(side="top",fill="x",padx=10,pady=5)

        tk.Label(master=date_frame,background="white",font=("Calibri",12,"bold"),text="Tarih    : ",width=10,anchor="e").pack(side="left")
        date_var = tk.StringVar(master=date_frame)
        date_var.set(today_date)
        date_ent = tk.Entry(master=date_frame,highlightthickness=1,font=("Calibri",12,"bold"),highlightcolor="red",foreground="blue",textvariable=date_var,relief="flat",background="white",highlightbackground="orange")
        date_ent.pack(fill="x",side="left",expand=True)

        #------------------------------------------------------------------------------
        self.status_frame = tk.Frame(master=add_frame,relief="flat",background="white")
        self.status_frame.pack(side="top",fill="x",padx=10,pady=5)

        tk.Label(master=self.status_frame,background="white",font=("Calibri",12,"bold"),text="Alan Seçin : ",width=10,anchor="e").pack(side="left")

        self.status_var = tk.StringVar(master=self.status_frame)
        if self.type == "gelir":
            self.status_variables = ["Öğrenci Taksit", "Öğrenci Ödeme", "Kurum Dışı D.S.", "Özel Ders Geliri",
                                "Ekstra İş","Sınıf-Kira","Sınav"]
        else:
            self.status_variables = ["Mutfak", "Kırtasiye", "Fatura - Elektrik", "Fatura - Su", "Fatura - Internet", "Fatura - Doğalgaz",
                                "Temizlik Malz.","Bakım","Tadilat", "Öğretmen Ödemesi"]
        self.status_ent = ttk.Combobox(self.status_frame,values=self.status_variables, textvariable=self.status_var)
        self.status_ent.set("Alan seçin veya yeni alan girin.")
        self.status_ent.pack(fill="x",side="left",expand=True)
        

        #------------------------------------------------------------------------------
        info_frame = tk.Frame(master=add_frame,relief="flat",background="white")
        info_frame.pack(side="top",fill="x",padx=10,pady=5)

        tk.Label(master=info_frame,background="white",font=("Calibri",12,"bold"),text="Açıklama : ",width=10,anchor="e").pack(side="left")

        info_var = tk.StringVar(master=info_frame)
        info_ent = tk.Entry(master=info_frame,highlightthickness=1,font=("Calibri",12,"bold"),highlightcolor="red",foreground="blue",textvariable=info_var,relief="flat",background="white",highlightbackground="orange")
        info_ent.pack(fill="x",side="left",expand=True)
        
        #------------------------------------------------------------------------------
        coast_frame = tk.Frame(master=add_frame,relief="flat",background="white")
        coast_frame.pack(side="top",fill="x",padx=10,pady=5)

        tk.Label(master=coast_frame,background="white",font=("Calibri",12,"bold"),text="Tutar    : ",width=10,anchor="e").pack(side="left")

        coast_var = tk.StringVar(master=coast_frame)
        coast_ent = tk.Entry(master=coast_frame,highlightthickness=1,font=("Calibri",12,"bold"),highlightcolor="red",foreground="blue",textvariable=coast_var,relief="flat",background="white",highlightbackground="orange")
        coast_ent.pack(fill="x",side="left",expand=True)





        #------------------------------------------------------------------------------


        save_buttons = tk.Button(master=add_frame,background=backgr,text="KAYDET",font=("Calibri",12,"bold"),command=lambda:kayit(
            date_ent.get(),self.au,self.type,self.status_ent.get(), info_var.get(),coast_var.get()
        ),relief="flat",border=0)
        save_buttons.pack(side="bottom",fill="x")
        


    def take(self):
        mydb = sq.connect('CDF.db')
        mycursor = mydb.cursor()
        query = f"Select * from payment_base where type like '{self.type}'"
        mycursor.execute(query)
        finded = sort_by_date(mycursor.fetchall())
        idcount = 0
        
        for i in finded:
            self.liste.insert(parent='',index="end",iid=idcount,values=(i[0],i[1],i[2],i[4],i[5],i[6]))
            idcount = idcount+1
        mydb.close()

    def find_to_delete(self):
        focussed = self.liste.focus()
        values = self.liste.item(focussed).get('values')
        pointer = values[0]

        mydb = sq.connect('CDF.db')
        mycursor = mydb.cursor()
        query = f"delete from payment_base where id = {pointer}"
        mycursor.execute(query)
        mydb.commit()
        mydb.close()
        
        case_page(self.panel)
        


    def create(self):
        self.topbar=tk.Frame(master=self.master,background="white")
        self.topbar.pack(side="top",fill="x")
        
        self.poz_section_add_btn = tk.Button(master=self.topbar,image=self.add_btn_image,relief="flat",background="white",command=self.save)
        self.poz_section_add_btn.img_reference = self.add_btn_image
        self.poz_section_add_btn.pack(side="left",fill="y")

        self.poz_section_sub_btn = tk.Button(master=self.topbar,image=self.sub_btn_image,relief="flat",background="white",command=self.find_to_delete)
        self.poz_section_sub_btn.img_reference = self.sub_btn_image
        self.poz_section_sub_btn.pack(side="left",fill="y")
        
        self.header = tk.Label(master=self.topbar, text=self.type.capitalize(),font=("Calibri",14),foreground="black",background="white").pack(fill="both",side="left")


        self.tree_based = tk.Frame(master=self.master,background="white",relief="flat")
        self.liste = ttk.Treeview(self.tree_based)
        self.xscrollx = tk.Scrollbar(self.liste,orient="horizontal",command=self.liste.xview,relief="flat")
        self.xscrollx.pack(side="bottom",fill="x")
        self.yscrolly = tk.Scrollbar(self.liste,orient="vertical",command=self.liste.yview,relief="flat")
        self.yscrolly.pack(side="right",fill="y")

        self.liste.configure(yscrollcommand=self.yscrolly.set)
        self.liste.configure(xscrollcommand=self.xscrollx.set)
        self.liste['columns'] = ('id','Tarih','İşleyen','Alan','Açıklama','Tutar')
        self.liste.column('#0',width=0,stretch=NO)
        


        self.liste.heading('id',text='id',anchor=W)
        self.liste.heading('Tarih',text='Tarih',anchor=W)
        self.liste.heading('İşleyen',text='İşleyen',anchor=W)
        self.liste.heading('Alan',text='Alan',anchor=W)
        self.liste.heading('Açıklama',text='Açıklama',anchor=W)
        self.liste.heading('Tutar',text='Tutar (₺)',anchor=W)
        for i in self.liste["columns"]:
            self.liste.column(i,width=10)
        
        
        self.liste.pack(fill="both",side="left",expand=True)

        self.take()


        return self.tree_based
    
    