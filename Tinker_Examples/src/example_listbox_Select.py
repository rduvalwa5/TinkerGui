'''
Created on Jul 11, 2017
https://stackoverflow.com/questions/7616541/get-selected-item-in-listbox-and-call-another-function-storing-the-selected-for
@author: rduvalwa2
'''
import tkinter as tk

class SampleApp(tk.Tk):
    def __init__(self, *args, **kwargs):
        tk.Tk.__init__(self, *args, **kwargs)
        lb = tk.Listbox(self)
        lb.insert("end", "one")
        lb.insert("end", "two")
        lb.insert("end", "three")
        lb.bind("<Double-Button-1>", self.OnDouble)
        lb.pack(side="top", fill="both", expand=True)

    def OnDouble(self, event):
        widget = event.widget
        selection=widget.curselection()
        value = widget.get(selection[0])
        print ("selection:", selection, ": '%s'" % value)

if __name__ == "__main__":
    app = SampleApp()
    app.mainloop()