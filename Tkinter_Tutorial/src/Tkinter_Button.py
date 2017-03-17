'''

Created on Mar 8, 2017
https://www.tutorialspoint.com/python/tk_button.htm
The Button widget is used to display buttons in your application.
@author: rduvalwa2
'''
import tkinter
from tkinter import messagebox

class button_example():
    def __init__(self, master=None):
        self.callMessageBox()
    def helloCallBack(self):
            messagebox.showinfo( "Hello Python", "Hello World")
    def callMessageBox(self):
        top = tkinter.Tk()
        B = tkinter.Button(top, text ="Hello", command = self.helloCallBack)
        B.pack()
        top.mainloop()

app = button_example()                
app.mainloop()