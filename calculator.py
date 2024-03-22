# calculator

import math
from tkinter import *
root = Tk()

root.title = "Calculator"
display = Entry(root)
display.grid(row=1, columnspan=20, sticky=W + E)

i = 0
def get_var(num):
    global i
    display.insert(i, num)
    i += 1
def clear_all():
    display.delete(0, END)

def get_op(opr):
    global i
    length = len(opr)
    display.insert(i, opr)
    i += length

def calculate():
    str1 = display.get()
    try:
        #a = parser.expr(str1).compile()
        result = eval(str1)
        clear_all()
        display.insert(0, result)
    except Exception:
        clear_all()
        display.insert(0, 'Error')

def undo():
    str2= display.get()
    if len(str2):
        new_str = str2[:-1]
        clear_all()
        display.insert(0, new_str)
    else:
        clear_all()
        display.insert(0, 'Error')


Button(root, text="1",width=5,height=3,command=lambda: get_var(1)).grid(row=6, column=0)
Button(root, text="2",width=5,height=3, command=lambda: get_var(2)).grid(row=6, column=1)
Button(root, text="3",width=5,height=3, command=lambda: get_var(3)).grid(row=6, column=2)
Button(root, text="4",width=5,height=3, command=lambda: get_var(4)).grid(row=5, column=0)
Button(root, text="5", width=5,height=3,command=lambda: get_var(5)).grid(row=5, column=1)
Button(root, text="6",width=5,height=3, command=lambda: get_var(6)).grid(row=5, column=2)
Button(root, text="7",width=5,height=3, command=lambda: get_var(7)).grid(row=4, column=0)
Button(root, text="8",width=5,height=3, command=lambda: get_var(8)).grid(row=4, column=1)
Button(root, text="9",width=5,height=3, command=lambda: get_var(9)).grid(row=4, column=2)
Button(root, text="0",width=5,height=3, command=lambda: get_var(0)).grid(row=7, column=1)
Button(root, text="C",width=5,height=3, command=lambda: clear_all()).grid(row=2, column=2)
Button(root, text="=",width=5,height=3, command=lambda: calculate()).grid(row=7, column=3)
Button(root, text="x", width=5,height=3,command=lambda: undo()).grid(row=2, column=3)
Button(root, text="+",width=5,height=3, command=lambda: get_op('+')).grid(row=6, column=3)
Button(root, text="-",width=5,height=3, command=lambda: get_op('-')).grid(row=5, column=3)
Button(root, text="*",width=5,height=3, command=lambda: get_op('*')).grid(row=4, column=3)
Button(root, text="/",width=5,height=3, command=lambda: get_op('/')).grid(row=3, column=3)
Button(root, text="pi", width=5,height=3,command=lambda: get_op('*3.14')).grid(row=2, column=1)
Button(root, text="2x",width=5,height=3, command=lambda: get_op('%')).grid(row=3, column=2)
Button(root, text="+/-",width=5,height=3, command=lambda: get_op('%')).grid(row=7, column=0)
Button(root, text=".",width=5,height=3, command=lambda: get_op('%')).grid(row=7, column=2)
Button(root, text="%",width=5,height=3, command=lambda: get_op('%')).grid(row=2, column=0)
Button(root, text="exp",width=5,height=3, command=lambda: get_op('**')).grid(row=3, column=0)
Button(root, text="sq", width=5,height=3,command=lambda: get_op('**2')).grid(row=3, column=1)

root.mainloop()
