# QR code generator

from tkinter import *
import pyqrcode
from PIL import ImageTk,Image
root=Tk()
frame=Frame(root)

def generate():
    link_name = name_entry.get()
    link = link_entry.get()
    file_name = link_name + ".png"
    url = pyqrcode.create(link)
    url.png(file_name,scale=8)
    image = ImageTk.PhotoImage(Image.open(file_name))
    image_label = Label(image=image)
    image_label.image = image
    canvas.create_window(200, 450, window=image_label)

canvas=Canvas(root,width=400,height=600)
canvas.pack()
app_label = Label(root, text="QR code Generator", fg='red', font=("Arial,30"))
canvas.create_window(200,50,window=app_label)
name_label=Label(root, text='Link name')

name_entry=Entry(root)
link_label=Label(root, text="Copy Link here")
link_entry=Entry(root)
canvas.create_window(200, 100, window=name_label)
canvas.create_window(200,130,window=name_entry)

canvas.create_window(200, 160, window=link_label)
canvas.create_window(200,180,window=link_entry)

b1=Button(root,text="Generate",command=generate)
canvas.create_window(150,230,window=b1)

b2=Button(root,text="Quit   ",command=frame.quit)
canvas.create_window(250,230,window=b2)

root.mainloop()