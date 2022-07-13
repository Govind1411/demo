
from tkinter import *
root= Tk()
#creating a label widget 

mylabel1=Label(root,text="Hello world")
mylabel2=Label(root,text="my name govind r nair ")

mylabel1.grid(row=0,column=0)
mylabel2.grid(row=1,column=5)

root.mainloop()