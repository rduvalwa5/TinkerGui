'''

The Label widget is used to provide a single-line caption for other widgets. It can also contain images.
'''

from tkinter import Tk
from tkinter import StringVar
from tkinter import Label
from tkinter import RAISED

root = Tk()

var = StringVar()
label = Label( root, textvariable=var, relief=RAISED )

var.set("  Hey!? \n How are you doing?")
label.pack()
root.mainloop()