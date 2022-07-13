from tkinter import *
root= Tk()
e=Entry(root,width=50,borderwidth=5)
e.pack()
e.insert(0,"enter your name: ")

def myclick():
    hello="hello"+ e.get()

    mylabel = Label(root,text=hello)
    mylabel.pack()


mybutton = Button(root,text="enter your name",command=myclick,fg="blue",bg="red")

mybutton.pack()

root.mainloop()