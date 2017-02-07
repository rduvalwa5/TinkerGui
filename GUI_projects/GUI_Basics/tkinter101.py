'''
Created on Dec 5, 2016

@author: rduvalwa2
'''
from tkinter import *
from tkinter.messagebox import showinfo
def reply():
    showinfo(title='popup', message='Button pressed!')

window = Tk()
button = Button(window, text='press', command=reply)
button.pack()
window.mainloop()