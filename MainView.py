import Tkinter as tk
from Tkinter import *
import tkFileDialog
from PIL import ImageTk, Image
import ImageItemView
import CutImage
import os

top = tk.Tk()
buttonsframe = tk.Frame(top)
cutsframe = tk.Frame(top)
imageitemsframe = tk.Frame(top)
propertyframe = tk.Frame(top)
top.minsize(width=666, height=666)
textlines = []
textframes = []
names = []
dir_name = os.getcwd()
dirtextprop = StringVar()
dirtextprop.set("Path: " + dir_name)
dirlabel = tk.Label(propertyframe, textvariable=dirtextprop,text=dirtextprop)

def browsedirectory():
    global dir_name
    dirbuff = tkFileDialog.askdirectory()
    if dirbuff != "":
        dir_name = dirbuff
    dirtextprop.set("Path: " + dir_name)
def addtextbox():
    global textframes
    f = Frame(cutsframe)
    nameLabel = Label(f,text="Name:")
    nameText=  Text(f, height=1,width=20)
    cutLabel = Label(f,text="Cuts:")
    cutText = tk.Text(f, height=1,width=30)
    textlines.append(cutText)
    names.append(nameText)

    nameLabel.pack(side=LEFT)
    nameText.pack(side=LEFT)
    cutLabel.pack(side=LEFT)
    cutText.pack(side=LEFT)
    f.pack(fill=BOTH)
    textframes.append(f)

def createimageitem(img,name):
    size = 200,200
    #bard = Image.open("test.bmp")
    img.thumbnail(size, Image.ANTIALIAS)
    bardejov = ImageTk.PhotoImage(img)
    f = ImageItemView.addimageitem(imageitemsframe,name, bardejov)
    f.pack()


def process():
    for i in range(0,len(textlines)):
        t = textlines[i].get("1.0",'end-1c')
        n = names[i].get("1.0",'end-1c')
        ci = CutImage.CutImage(t)
        path = os.path.join(dir_name, n + "." + "bmp")
        ci.image.save(path)
        i = ci.image
        createimageitem(i,n)


def deletelastline():
    if len(textframes) > 1:
        frm = textframes[-1]
        frm.pack_forget()
        frm.destroy()
        del textframes[-1]


# Code to add widgets will go here...
addcutline = tk.Button(buttonsframe, text="Add line", command = addtextbox)
processButton = tk.Button(buttonsframe,text="Process",command=process)
browsedirbutton = tk.Button(buttonsframe, text="Open Folder...", command=browsedirectory)
deletelastlinebutton =  tk.Button(buttonsframe,text="Delete line",command=deletelastline)

dirlabel.pack(side=LEFT)
propertyframe.pack(side=TOP, fill=X)

browsedirbutton.pack(side=LEFT)

cutsframe.pack(fill=X)
addcutline.pack(side=RIGHT)
deletelastlinebutton.pack(side=RIGHT)

#createimageitem()
imageitemsframe.pack(fill=X)
addtextbox()
processButton.pack(side=RIGHT)
addcutline.pack(side=RIGHT)

buttonsframe.pack(fill=BOTH, side=BOTTOM)
top.mainloop()