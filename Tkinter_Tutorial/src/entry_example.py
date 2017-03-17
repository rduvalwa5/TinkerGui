'''

The Entry widget is used to display a single-line text field for accepting values from a user.
https://www.tutorialspoint.com/python/tk_entry.htm
'''
from tkinter import *

top = Tk()
L1 = Label(top, text="User Name")
L1.pack( side = LEFT)
E1 = Entry(top, bd =5)

E1.pack(side = RIGHT)

top.mainloop()