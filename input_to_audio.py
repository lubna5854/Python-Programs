# converting your input to audio

from gtts import gTTS
import os

from tkinter import *
root=Tk()
canvas=Canvas(root,width=400,height=400)
canvas.pack()

def text_to_speech():
    text=entry.get()
    output=gTTS(text=text,lang='ml',slow=False)
    output.save('input.mp4')
    os.system('start input.mp4')

entry=Entry(root)
canvas.create_window(200,180,window=entry)
b1=Button(text="Start",command=text_to_speech)
canvas.create_window(200,230,window=b1)
root.mainloop()