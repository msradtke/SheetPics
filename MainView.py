import Tkinter as tk
from Tkinter import *
import tkFileDialog
from PIL import ImageTk, Image
import ImageItemView
import CutImage
import os
from stat import S_IREAD, S_IRGRP, S_IROTH,S_IWUSR,S_IWRITE

top = tk.Tk()
buttonsframe = tk.Frame(top)
cutsframe = tk.Frame(top)
canvasimageitemframe = tk.Frame(top)
propertyframe = tk.Frame(top)
top.minsize(width=666, height=666)

scale = 5
textlines = []
textframes = []
imageitemframes = []
names = []
dir_name = os.getcwd()
dirtextprop = StringVar()
dirtextprop.set("Path: " + dir_name)

subdirstring = StringVar()
subdirlabel = tk.Label(propertyframe,text="Subdirectory:")
subdirentry = tk.Entry(propertyframe,textvariable=subdirstring)


dirlabel = tk.Label(propertyframe, textvariable=dirtextprop,text=dirtextprop)

scaletextvar = StringVar()
scaleframe = tk.Frame(top)
scalelabel = tk.Label(scaleframe, text="Scale:")
scalentry = tk.Entry(scaleframe, textvariable=scaletextvar)
scaletextvar.set(str(scale))


def on_configure(event):
    # update scrollregion after starting 'mainloop'
    # when all widgets are in canvas
    canvas.configure(scrollregion=canvas.bbox('all'))

# --- create canvas with scrollbar ---
canvas = tk.Canvas(canvasimageitemframe)
canvas.pack(side=tk.RIGHT,fill=BOTH,expand=TRUE)

imageitemsframe = tk.Frame(canvas)
scrollbar = tk.Scrollbar(canvas, command=canvas.yview)
scrollbar.pack(side=tk.RIGHT, fill=Y)

canvas.configure(yscrollcommand=scrollbar.set)

# update scrollregion after starting 'mainloop'
# when all widgets are in canvas
imageitemsframe.bind("<Configure>", lambda event, canvas=canvas: on_configure(canvas))
# --- put frame in canvas ---


canvas.create_window((4,4), window=imageitemsframe, anchor='nw')

def browsedirectory():
    global dir_name
    dirbuff = tkFileDialog.askdirectory()
    if dirbuff != "":
        dir_name = dirbuff
    dirtextprop.set("Path: " + dir_name)
def addtextbox():
    global textframes
    global textlines

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
    global imageitemframes
    size = 200,200
    #bard = Image.open("test.bmp")
    img.thumbnail(size, Image.ANTIALIAS)
    bardejov = ImageTk.PhotoImage(img)
    f = ImageItemView.addimageitem(imageitemsframe,name, bardejov)
    f.pack()
    imageitemframes.append(f)


def process():
    global scaletextvar
    global subdirentry
    subdir = subdirentry.get()
    for i in range(0,len(textlines)):
        t = textlines[i].get("1.0",'end-1c')
        n = names[i].get("1.0",'end-1c')
        ci = CutImage.CutImage(t,int(scaletextvar.get()))

        path = dir_name
        filepath = os.path.join(dir_name, n + "." + "bmp")
        if not subdir == "":
            path = os.path.join(dir_name, subdir)
            filepath = os.path.join(dir_name, subdir + os.sep + n + "." + "bmp")
        if not os.path.exists(path):
            os.makedirs(path)
            #os.chmod(path, S_IWUSR | S_IWRITE)
        ci.image.save(filepath)
        i = ci.image
        createimageitem(i,n)


def deletelastline():
    if len(textframes) > 1:
        frm = textframes[-1]
        frm.pack_forget()
        frm.destroy()
        del textframes[-1]
        del textlines[-1]
        del names[-1]


def clearitems():
    clearlist(imageitemframes)
    clearlist(textframes)
    del imageitemframes[:]
    del textframes[:]
    del textlines[:]
    del names[:]
    addtextbox()


def clearlist(list):
    for frm in list:
        frm.pack_forget()
        frm.destroy()


def opendirectory():
    global dir_name
    os.startfile(dir_name)

# Code to add widgets will go here...
addcutline = tk.Button(buttonsframe, text="Add line", command = addtextbox)
processButton = tk.Button(buttonsframe,text="Process",command=process)
browsedirbutton = tk.Button(buttonsframe, text="Set Folder...", command=browsedirectory)
deletelastlinebutton = tk.Button(buttonsframe,text="Delete line",command=deletelastline)
clearitemsbutton = tk.Button(buttonsframe,text="Clear All",command=clearitems)
opendirbutton = tk.Button(buttonsframe, text="Open...", command=opendirectory)

subdirentry.pack(side=RIGHT,anchor=E)
subdirlabel.pack(side=RIGHT,anchor=E)

dirlabel.pack(side=LEFT,anchor=W)
propertyframe.pack(fill=BOTH, pady=(5, 15))
opendirbutton.pack(side=LEFT)

scaleframe.pack(anchor=W)
scalelabel.pack(side=LEFT)
scalentry.pack(side=LEFT)


browsedirbutton.pack(side=LEFT)

cutsframe.pack(fill=X)
addcutline.pack(side=RIGHT)
deletelastlinebutton.pack(side=RIGHT)

#createimageitem()
#imageitemsframe.pack(fill=BOTH)
canvasimageitemframe.pack(fill=BOTH,expand=1)
addtextbox()
processButton.pack(side=RIGHT)
addcutline.pack(side=RIGHT)

clearitemsbutton.pack(side=RIGHT)
buttonsframe.pack(fill=BOTH, side=BOTTOM)
top.mainloop()