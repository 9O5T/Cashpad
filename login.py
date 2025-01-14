
from tkinter import *
import tkinter as tk
from tkinter import ttk
from PIL import ImageTk, Image


def login_win(users):

    def log():
        global username_full
        username = username_ent.get()
        password = password_ent.get()
        # Kullanici adi aramasi
        for user in users:
            if username == user[0] and password == user[2]:
                LOP.set(True)
                username_full = user[1]
                login_window.destroy()

        
        if LOP.get() == False :
            tk.messagebox.showerror(title="Hatalı Giriş!", message="Kullanıcı adı veya şifre yanlış!")
                



    def mouse_on1(e):
        username_ent.delete(0,'end')
    def mouse_on2(e):
        password_ent.delete(0,"end")
    def mouse_off1(e):
        text = username_ent.get()
        if text == '':
            username_ent.insert(0,"Kullanıcı Adı")
    def mouse_off2(e):
        text = password_ent.get()
        if text == '':
            password_ent.insert(0,"Şifre")



    login_window = tk.Tk()
    login_window.title("Cashpad Giriş Ekranı")

    icon = PhotoImage(file="images/Cashpad.png")
    login_window.iconphoto(False,icon)

    screen_h = login_window.winfo_screenheight()
    screen_w = login_window.winfo_screenwidth()

    app_w = int(screen_w/3)
    app_h = int(screen_h/1.25)

    login_window.geometry(f"{app_w}x{app_h}+{int(screen_w*(0.5))-int(app_w*(0.5))}+{int(screen_h*(0.5))-int(app_h*(0.5))}")
    login_window.minsize(width=app_w, height=app_h)
    login_window.configure(background="white")

    login_image = Image.open('images/fingerprint.png')
    login_image = login_image.resize((app_w-int(app_w/1.5),app_w-int(app_w/1.5)))
    login_image = ImageTk.PhotoImage(login_image)
    tk.Label(login_window,image=login_image,background="white").pack(pady=50)

    username_ent = tk.Entry(master=login_window,relief="flat",background="white",foreground="black",border=3,highlightcolor="purple",highlightthickness=1,width=30,
                            font=("Calibri",14),justify="center",highlightbackground="RoyalBlue1")
    username_ent.insert(0,"Kullanıcı Adı")
    username_ent.pack(padx=50,fill="x")
    password_ent =  tk.Entry(master=login_window,relief="flat",background="white",foreground="black",border=1,highlightcolor="purple",highlightthickness=1,width=30,
                             font=("Calibri",14),show='\u25C9',justify="center",highlightbackground="RoyalBlue1")
    password_ent.pack(padx=50,pady=20,fill="x")

    username_ent.bind('<FocusIn>',mouse_on1)
    password_ent.bind('<FocusIn>',mouse_on2)
    username_ent.bind('<FocusOut>',mouse_off1)
    password_ent.bind('<FocusOut>',mouse_off2)

    LOP = tk.BooleanVar(master=login_window)

    LogIn_button = tk.Button(master=login_window,text="Giriş Yap",border=0,foreground="white",background="#2ABDE1",font=("Calibri",14),relief="flat",command=log)
    LogIn_button.pack(pady=30,padx=50,fill="x")

    login_window.mainloop()
    return LOP.get(),username_full