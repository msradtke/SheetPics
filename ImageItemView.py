import Tkinter
from Tkinter import Tk, Label, BOTH,X, Text,INSERT
from Tkinter import *
from ttk import Frame, Style
from PIL import ImageTk, Image

def addimageitem(parent, name, i):
    f = Frame(parent)
    f.columnconfigure(0,pad=3)
    f.columnconfigure(1,pad=3,weight=10)
    f.columnconfigure(2,pad=3,weight=10)

    nameLabel = Label(f,text=name)
    picLabel = Label(f,text=name,image=i)
    picLabel.image=i
    picLabel.text = name
    picLabel.grid(column=1,sticky=W)
    nameLabel.grid(column=0, sticky=E)
    f.pack(fill=BOTH, padx=5, pady=5)
    return f
