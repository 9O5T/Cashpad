from tkinter import *
import tkinter as tk
from tkinter import ttk
import sqlite3 as sq
import matplotlib.pyplot as plt 
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg as fct
from datetime import datetime
from calendar import monthrange
from PIL import ImageTk, Image

from login import login_win
from elements import cbutton
from parts import Left_Panel

import os
import cashpad_DFB as ndb


db_path = 'CDF.db'
if os.path.exists(db_path):
    mydb = sq.connect('CDF.db')
    mycursor = mydb.cursor()
else:
    ndb.database_build()
    mydb = sq.connect('CDF.db')
    mycursor = mydb.cursor()


users = [
    ['admin','User','123456']
    ]

login = login_win(users)
active_user = login[1]
if login[0]:
    main_window = tk.Tk()
    # images and resource
    image_for_student_profile = Image.open("images/student.png")
    image_for_student_profile = image_for_student_profile.resize((100,100))
    image_for_student_profile = ImageTk.PhotoImage(image_for_student_profile)

    image_for_special_lesson_pre = Image.open("images/special_class.png")
    #image_for_special_lesson = image_for_special_lesson.resize((100,100))
    image_for_special_lesson = ImageTk.PhotoImage(image_for_special_lesson_pre)

    tik = Image.open('images/tic.png')
    tik = ImageTk.PhotoImage(tik)

    close_btn_image = Image.open('images/close_button.png')
    close_btn_image = close_btn_image.resize((20,20))
    close_btn_image = ImageTk.PhotoImage(close_btn_image)



    icon = PhotoImage(file="images/Cashpad.png")
    main_window.iconphoto(False,icon)

    main_window.title("Cashpad")

    screen_h = main_window.winfo_screenheight()
    screen_w = main_window.winfo_screenwidth()

    app_w = int(screen_w/1.25)
    app_h = int(screen_h/1.25)

    main_window.geometry(f"{app_w}x{app_h}+{int(screen_w*(0.5))-int(app_w*(0.5))}+{int(screen_h*(0.5))-int(app_h*(0.5))}")
    main_window.minsize(width=app_w, height=app_h)
    main_window.config(background="white")

    #######


    #######




    #btn = cbutton(main_window,"naber","white","red").create()
    #btn.place(relx=0,rely=0,relwidth=0.1,relheight=0.05)
    base_frame = tk.Frame(main_window,background="white",highlightthickness=0,border=0)
    base_frame.place(relx=0.051,rely=0,relwidth=0.949,relheight=1.0) 

    control_panel = Left_Panel(main_window,base=base_frame, background="lavender",au=active_user).create()
    control_panel.place(relx=0,rely=0,relwidth=0.05,relheight=1.0)

    
    
    main_window.mainloop()


