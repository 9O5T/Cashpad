from tkinter import *
import tkinter as tk
from tkinter import ttk
from datetime import datetime

class cbutton:
    def __init__(self, master, image, background,command):
        self.master=master
        self.background = background
        self.image = image
        self.relief = "flat"
        self.command = command

    def create(self):
        self.btn = tk.Button(self.master, image=self.image,
                              background = self.background,
                              relief=self.relief,
                              highlightthickness=0,
                              border=0,command=self.command)
                              
        return self.btn
    
def clear_frame(frame_base):
        for widgets in frame_base.winfo_children():
            widgets.destroy()

def sort_by_date(data):
    return sorted(data, key=lambda x: datetime.strptime(x[1], '%d/%m/%Y'))