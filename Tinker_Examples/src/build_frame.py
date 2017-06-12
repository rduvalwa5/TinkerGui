'''
Created on Jun 11, 2017

@author: rduvalwa2
'''
from tkinter import *

top_frame = Frame()
label1 = Label(top_frame, text="ID")
label1.pack(side=RIGHT)
bottom_frame = Frame()
bottom_frame.pack(side=TOP)
QUIT = Button(bottom_frame, text="Quit", command=quit, state='active')
QUIT.pack(side=LEFT)
handleb = Button(bottom_frame, text="Get Album")
handleb.pack(side=LEFT)

root = Tk()
root.geometry("200x100+30+30")
mainloop()  
