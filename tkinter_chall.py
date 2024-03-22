# using tkinter create an interface for username,password,confirm password,email,age, and buttons login and cancel

from tkinter import *
root=Tk()

uname=Label(root,text="User name:")
password=Label(root,text="Pass word:")
con_pwd=Label(root,text="Confirm password:")
age=Label(root,text="User Age:")
email=Label(root,text="User Email:")

e1=Entry(root)
e2=Entry(root)
e3=Entry(root)
e4=Entry(root)
e5=Entry(root)

uname.grid(row=0,column=0)
e1.grid(row=0,column=1)
password.grid(row=1,column=0)
e2.grid(row=1,column=1)
con_pwd.grid(row=2,column=0)
e3.grid(row=2,column=1)
age.grid(row=3,column=0)
e4.grid(row=3,column=1)
email.grid(row=4,column=0)
e5.grid(row=4,column=1)

but=Button(root,text="Login")
but.grid(row=5,column=0)
but2=Button(root,text="Cancel")
but2.grid(row=5,column=1)

root.mainloop()