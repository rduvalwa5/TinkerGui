'''
Created on Jan 29, 2017
from dialogue.py
@author: rduvalwa2
'''
from tkinter import *
from tkinter.simpledialog import Dialog

class MyDialog(Dialog):
    def body(self, master):
        self.result = None
        for r in range(5):
            for c in range(5):
                b = Button(master, text="Row {0} Col {1}".format(r, c))
                b.grid(row=r, column=c)
        print("Dialog created")

    def apply(self):
        self.result = "OK"

        self.d_button = Button(self, text="Dialog...", command=self.create_dialog)
        self.d_button.pack({"side": "left"})

class MyColors(Dialog):
    def body(self, master):
        self.result = None
        for r in range(5):
            for c in range(5):
                b = Button(master, text="Row {0} Col {1}".format(r, c))
                b.grid(row=r, column=c)
        print("Colors created")

    def apply(self):
        self.result = "OK"
        self.c_button = Button(self, text="Colors...", command=self.create_dialog)
        self.c_button.pack({"side": "left"})
        
class Application(Frame):
    def create_dialog(self):
        d = MyDialog(self)
        print(d.result)
        
    def create_Colors(self):
        c = MyColors(self)
        print(c.result)

    def create_widgets(self):
        
        self.c_button = Button(self, text="Colors", fg = "black", bg = "green", command=self.create_Colors())
        self.c_button.pack({"side": "left"})
        
        self.d_button = Button(self, text="Dialog...", command=self.create_dialog)
        self.d_button.pack({"side": "left"})

        self.QUIT = Button(self, text="Quit", fg="red",bg="black", command=self.quit)
        self.QUIT.pack({"side": "left"})

    def __init__(self, master=None):
        Frame.__init__(self, master)
        self.grid()
        self.create_widgets()

root = Tk()
app = Application(master=root)
app.mainloop()
