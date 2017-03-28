from tkinter import *
from tkinter import messagebox
'''
from tkinter import messagebox
messagebox.showinfo("Title", "a Tk MessageBox")
''' 
import tkinter

top = tkinter.Tk()

def helloCallBack():
        messagebox.showinfo("Hello Python", "Hello World")

B = tkinter.Button(top, text="Hello", command=helloCallBack)
B.pack()
B.place(bordermode=OUTSIDE, height=100, width=100)
top.mainloop()
