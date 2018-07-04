#q1  Create a dict with name and mobile number.Define a GUI interface using tkinter and pack the label and create a scrollbar to scroll the list of keys in the dictionary.


import tkinter
from tkinter import *

root=Tk()
root.title("Dictionary")
root.geometry('200x200')
a=Label(root,text="Dictionary \nNames and Mobile Number",bg="yellow")
a.pack()
f1=Frame(root)
f1.pack(side=TOP)

w=Scrollbar(f1,orient="vertical",)
w.pack(side=RIGHT,fill=Y)
mylist=Listbox(f1,width=30 , font=("Helvetica", 12),yscrollcommand=w.set)



d={"gayatri":999,"astha":895,"niku":567,"harpreet":5658,"bhuvi":6576,"geetu":45747,"rohit":5345,"kamini":45678,"ram":4586,"sahil":809687}

for key in d:
    mylist.insert(END,'{}: {}'.format(key, d[key]))
mylist.pack(side=LEFT,fill=BOTH)
w.config(command=mylist.yview)
root.mainloop()