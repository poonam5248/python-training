#q3  Create a frame using tkinter with any label text and two buttons.One to exit and other to change the label to some other text.


import tkinter
from tkinter import *
import sys

def exit():
    sys.exit()


def click():
    a.config(text="WELCOME!")


root=Tk()
root.geometry("400x400")

a=Label(root,text="HELLO WORLD !",width=150,fg="red")
a.pack()
f1=Frame(root)
f1.pack(side=TOP)

b1=Button(f1,width=30,text="exit!",bg="pink",command=exit)
b1.pack()

b2=Button(f1,width=30,text="label",bg="cyan",command=click)
b2.pack()

root.mainloop()