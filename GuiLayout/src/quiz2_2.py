'''
Created on Jan 8, 2013
How would you configure frame F in a grid layout to occupy three rows and two columns starting at row 3, column 2?
Do the row and column numbers used with the grid layout manager need to be contiguous?
image.grid(row=0, column=2, columnspan=2, rowspan=2,
               sticky=W+E+N+S, padx=5, pady=5)
http://effbot.org/tkinterbook/grid.htm
@author: rduval
'''
from tkinter import  *

ALL = N+S+W+E

class Application(Frame):
    def __init__(self, master=None):
        Frame.__init__(self, master)
        self.master.rowconfigure(2, weight=2)
        self.master.columnconfigure(0, weight=1)
        self.grid(sticky=ALL)
        for r in range(9):
            self.rowconfigure(r, weight=1)
            Label(self, text="{0}".format(r)).grid(row=r, column=0, sticky=ALL)
        self.rowconfigure(5, weight=1)
        for c in range(9):
            self.columnconfigure(c, weight=1)
            Label(self, text="{0}".format(c)).grid(row=9, column=c, sticky=ALL)
        f = Frame(self, bg="red")
        f.grid(row=3, column=3, rowspan=3, columnspan=3, ipady=1,padx=1,sticky=N+S+W+E)

                
root = Tk()
app = Application(master=root)
app.mainloop()