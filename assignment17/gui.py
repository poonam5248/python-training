#q1 Write a python program using tkinter interface to write Hello World and a exit button that closes the interface.

import tkinter
from tkinter import *
import sys
def exit():
    sys.exit()

root=Tk()
root.title("My app")
root.geometry("400x400")
root.resizable(False,False)
a=Label(root,text="HELLO WORLD !",width=150)
a.pack()
b=Button(root,text="click!",command=exit)
b.pack()

root.mainloop()