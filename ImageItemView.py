import Tkinter
from Tkinter import Tk, Label, BOTH,X, Text,INSERT
from Tkinter import *
from ttk import Frame, Style
from PIL import ImageTk, Image

def addimageitem(parent, name, i):
    s = Style()
    #s.configure("My.TFrame", background="red")
    f = Frame(parent, style="My.TFrame")
    f.columnconfigure(0, pad=3, weight=0)
    f.columnconfigure(1, pad=3, weight=2)
    f.columnconfigure(2, pad=3, weight=2)
    f.rowconfigure(0, pad=3, weight=1)

    nameLabel = Label(f, text=name, wraplength=125, width=15)
    picLabel = Label(f, text=name, image=i)
    picLabel.image = i
    picLabel.text = name
    picLabel.grid(row=0, column=1,sticky="EW")
    nameLabel.grid(row=0, column=0,sticky=N+S)
    f.pack(fill=BOTH, padx=5, pady=5)
    return f