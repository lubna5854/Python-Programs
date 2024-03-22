from tkinter import *
root=Tk()

toolbar=Frame(root,bg="red")
b1=Button(toolbar,text="Crop")
b1.pack(side=LEFT,padx=2,pady=3)
toolbar.pack(side=TOP,fill=X)

statusbar=Label(root,text="This is statusbar",relief=SUNKEN,bd=2,anchor=W)
statusbar.pack(side=BOTTOM,fill=X)

root.mainloop()
