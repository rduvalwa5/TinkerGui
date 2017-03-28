'''
Created on Jan 13, 2013
Lesson 8, Project 1

Here are your instructions:
Write a GUI-based program to build a window layout as shown below. When the frame is resized, the buttons should stay the same height
and expand sideways. Frame 1 and  Frame 2 should always be the same height and width as each other, and Frame 3 should be half as wide
again as they are (i.e. 150% wider, as shown below).  Labeling each Frame is optional / good exercise.
-
+---------------------+--------------------------------+
|                     |                                |
|                     |                                |
|                     |                                |
|      Frame 1        |                                |
|                     |                                |
|                     |                                |
|                     |                                |
+---------------------+               Frame 3          |
|                     |                                |
|                     |                                |
|                     |                                |
|     Frame 2         |                                |
|                     |                                |
|                     |                                |
+----------+----------+----------+----------+----------+
| Button 1 | Button 2 | Button 3 | Button 4 | Button 5 |
+----------+----------+----------+----------+----------+

@author: rduvalwa2
'''
from tkinter import *

# ALL = N+S+W+E
 
class Application(Frame):
    def __init__(self, master=None):
        Frame.__init__(self, master)
        self.master.rowconfigure(0, weight=1)
        self.master.columnconfigure(0, weight=1)
        self.grid(sticky=N + S + W + E)
        for r in range(14):
            self.rowconfigure(r, weight=1)
            if r == 7:
                Label(self, text="".format(r)).grid(row=r, column=3)
            else:
                Label(self, text="".format(r)).grid(row=r, column=0)
        self.rowconfigure(5, weight=1)
        for c in range(1, 6):
            self.columnconfigure(c, weight=1)
            Button(self, text="Button {0}".format(c)).grid(row=14, column=c, sticky=E + W)
        frame1 = Frame(self, bg="red")
        frame1.grid(row=0, column=1, rowspan=7, columnspan=2, sticky=N + S + W + E)
        frame2 = Frame(self, bg="blue")
        frame2.grid(row=7, column=1, rowspan=7, columnspan=2, sticky=N + S + W + E) 
        frame3 = Frame(self, bg="yellow")
        frame3.grid(row=0, column=3, rowspan=14, columnspan=3, sticky=N + S + W + E)        

root = Tk()
app = Application(master=root)                
app.mainloop()
