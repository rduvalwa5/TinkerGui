'''
Created on Jan 8, 2013
tkgrid.py 
Demo of Grid Layout
@author: rduval
'''
from tkinter import  *

def colorgren():
    while True:
        yield "red"
        yield "blue"
        yield "yellow"
        yield "purple"
class Application(Frame):
    
    def __init__(self, master=None):
        colors = colorgren()
        Frame.__init__(self,master)
        self.grid()
        for r in (1, 22, 333, 444):
            for c in (1,22,333, 444):
                txt = "Item{0}, {1}".format(r,c)
                l = Label(self, text=txt, bg=next(colors))
#                l.grid(row=r, column=c)
                l.grid(row=r, column=c, sticky=E+W)


                
root = Tk()
app = Application(master=root)
app.mainloop()