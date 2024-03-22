# using tkinter create a program for school with three buttons

from tkinter import *
class school:
    def __init__(self,root):
        frame=Frame(root)
        self.name=Label(root,text="User name:")
        self.clas=Label(root,text="Class: ")
        self.pwd=Label(root,text="Password: ")

        self.e1=Entry(root)
        self.e2=Entry(root)
        self.e3=Entry(root)

        self.click=Button(root,text="Click",command=self.clic_msg)
        self.cancel=Button(root,text="Cancel",command=self.can_msg)
        self.exit=Button(root,text="Exit",command=frame.quit)

        self.name.grid(row=0, column=0)
        self.e1.grid(row=0, column=1)
        self.clas.grid(row=1,column=0)
        self.e2.grid(row=1,column=1)
        self.pwd.grid(row=2,column=0)
        self.e3.grid(row=2,column=1)

        self.click.grid(row=3,column=0)
        self.cancel.grid(row=3,column=1)
        self.exit.grid(row=3,column=5)

    def clic_msg(self):
        print("Click here")

    def can_msg(self):
        print("Cancelled")

root=Tk()
obj=school(root)
root.mainloop()