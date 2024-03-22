from tkinter import *

def fun():
    print("Hello how are you")

root=Tk()
Label(root,text="Hello world").pack()
f1=Frame(root)
f1.pack()
b1=Button(root,text="Click",fg="red",bg="black",command=fun)
b1.pack()
root.mainloop()