#q4 Write a python program using tkinter interface to take an input in the GUI program and print it.

import tkinter
from tkinter import *

def show():
    print(entry.get())

root=Tk()
root.geometry("400x400")


entry=Entry(root,width=40)
entry.pack()
b=Button(root,text="click",width=20,bg="orange",command=show)
b.pack(side= TOP)

root.mainloop()