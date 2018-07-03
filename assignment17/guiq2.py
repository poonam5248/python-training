#q2 Write a python program to in the same interface as above and create a action when the button is click it will display some text.

import tkinter
from tkinter import *

def show():
    print("Hey Beautiful!")

root= Tk()
root.geometry("250x250")
b=Button(root,text="click",bg="cyan",fg="black",command=show)
b.pack()

root.mainloop()