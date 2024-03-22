#Menu Program

from tkinter import *
root=Tk()
frame=Frame(root)

def new_msg():
    print("This is new project")

def copy_msg():
    print("This is copy")

def open_msg():
    print("Open project")


mymenu=Menu(root)
root.configure(menu=mymenu)
filemenu=Menu(mymenu)

mymenu.add_cascade(label="File",menu=filemenu)
filemenu.add_command(label="New",command=new_msg)
filemenu.add_command(label="Open",command=open_msg)
filemenu.add_separator()
filemenu.add_command(label="Save")
filemenu.add_command(label="Save as")
filemenu.add_separator()
filemenu.add_command(label="Print")
filemenu.add_command(label="Exit",command=frame.quit)

editmenu=Menu(mymenu)
mymenu.add_cascade(label="Edit",menu=editmenu)
editmenu.add_command(label="Cut")
editmenu.add_command(label="Copy",command=copy_msg)
editmenu.add_command(label="Paste")
editmenu.add_separator()
editmenu.add_command(label="Delete")
editmenu.add_separator()
editmenu.add_command(label="find")
editmenu.add_command(label="Select All")

viewmenu=Menu(mymenu)
mymenu.add_cascade(label="View",menu=viewmenu)
viewmenu.add_command(label="Tool windows")
viewmenu.add_command(label="Appearance")
viewmenu.add_separator()
viewmenu.add_command(label="Quick definition")
viewmenu.add_command(label="Recent files")
viewmenu.add_separator()
viewmenu.add_command(label="help")

codemenu=Menu(mymenu)
mymenu.add_cascade(label="Code",menu=codemenu)
codemenu.add_command(label="Generate")
codemenu.add_command(label="Inspect code")
codemenu.add_command(label="Analyze code")
codemenu.add_command(label="Code cleanup")

runmenu=Menu(mymenu)
mymenu.add_cascade(label="Run",menu=runmenu)
runmenu.add_command(label="Run...")
runmenu.add_command(label="Debug...")


root.mainloop()

