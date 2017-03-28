'''
Created on Jan 15, 2013
Lesson 8 Project
@author: rduval
'''
from tkinter import *

class Application(Frame):
    def __init__(self, master=None):
        Frame.__init__(self, master)
        self.master.rowconfigure(0, weight=1)
        self.master.columnconfigure(0, weight=1)
        self.grid(sticky=N + S + W + E)
        for r in range(14):
            self.rowconfigure(r, weight=1)
            if r == 7:
                Label(self, text="Frame 1".format(r)).grid(row=r, column=3)
            else:
                Label(self, text="".format(r)).grid(row=r, column=0)
        self.rowconfigure(5, weight=1)
        for c in range(1, 6):
            self.columnconfigure(c, weight=1)
            Button(self, text="Button {0}".format(c)).grid(row=14, column=c, sticky=E + W)
        frame1 = Frame(self, bg="red")
        frame1.grid(row=0, column=1, rowspan=7, columnspan=2, sticky=N + S + W + E)
        fr_label = Label(frame1, text="Frame 1", fg="black", bg="Red")
        fr_label.grid()
        frame2 = Frame(self, bg="blue")
        frame2.grid(row=7, column=1, rowspan=7, columnspan=2, sticky=N + S + W + E) 
        fr_label2 = Label(frame2, text="Frame 2", fg="black", bg="blue")
        fr_label2.grid()
        frame3 = Frame(self, bg="yellow")
        frame3.grid(row=0, column=3, rowspan=14, columnspan=3, sticky=N + S + W + E)        
        fr_label3 = Label(frame3, text="Frame 3", fg="black", bg="yellow")
        fr_label3.grid()

root = Tk()
app = Application(master=root)                
app.mainloop()
