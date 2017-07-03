import Tkinter as tk
from Tkinter import *
from PIL import ImageTk, Image
import ImageItemView
import CutImage

top = tk.Tk()
cutsframe = tk.Frame(top)
imageitemsframe = tk.Frame(top)
top.minsize(width=666, height=666)
textlines = []
names = []
def addtextbox():
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
        i = ci.image
        createimageitem(i,n)

# Code to add widgets will go here...
button = tk.Button(top, text="testing",command = addtextbox)
processButton = tk.Button(top,text="process",command=process)



cutsframe.pack(fill=X)
button.pack()


#createimageitem()
imageitemsframe.pack(fill=X)
addtextbox()
processButton.pack()
top.mainloop()

