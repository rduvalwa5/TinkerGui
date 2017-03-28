'''
Here are your instructions:
Starting with the project you created at the end of the last lesson, add components 
to the existing framework so that:
A. 
   When the areas occupied by Frame 1 or Frame 2 are clicked with mouse button 1,
   the program should print which frame was clicked and the X and Y coordinates 
   (relative to the Frame).
B.
   Frame 3 should contain:
   1. an Entry 
   2. and a Text widget. 
   3. When the button now labeled "Open" is clicked
      the content of the Entry should be used as a file name
      and the content of the file (if any) displayed in the Text widget
C.
   The Entry and Text widgets should completely fill Frame 3 
   and continue to do so even as the application window is resize.
D. 
   The color of the text displayed in Frame 3's Text widget should change 
   appropriately when the "Red," "Blue," "Green," or "Black" buttons are clicked.
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
|    Red   |   Blue   |  Green   |  Black   |   Open   |
+----------+----------+----------+----------+----------+
@author: rduvalwa2
'''
from tkinter import *
 
class Application(Frame):
    def __init__(self, master=None):
        
        def frame1ClickHandler(event):
            print("Frame 1", event.x, event.y)
        def frame2ClickHandler(event):
            print("Frame 2", event.x, event.y)
        def makeRed():
            print("Clicked Red")
            self.text_in.config(fg="red")
        def makeBlue():
            print("Clicked Blue")
            self.text_in.config(fg="blue")
        def makeGreen():
            print("Clicked Green")
            self.text_in.config(fg="green")
        def makeBlack():
            print("Clicked Black")
            self.text_in.config(fg="black")
        def openHandler():
            print("Clicked open")
            print("/users/rduvalwa2/testFile.txt")
            file_name = self.text_in.get()
            print(file_name)
            try:
                f = open(file_name)
                s = f.read()
                print(s)
                self.text_in2.insert(END, s)
            except IOError as e:
                    self.text_in2.insert(END, e)
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
            myButtonTxt = ['Red', 'Blue', 'Green', 'Black', 'Open']
            myButtonCmd = [makeRed, makeBlue, makeGreen, makeBlack, openHandler]
            Button(self, text=myButtonTxt[c - 1].format(c), command=myButtonCmd[c - 1]).grid(row=14, column=c, sticky=E + W)
        frame1 = Frame(self, bg="red")
        frame1.grid(row=0, column=1, rowspan=7, columnspan=2, sticky=N + S + W + E)
        frame1.bind("<Button-1>", frame1ClickHandler)
        frame2 = Frame(self, bg="blue")
        frame2.grid(row=7, column=1, rowspan=7, columnspan=2, sticky=N + S + W + E) 
        frame2.bind("<Button-1>", frame2ClickHandler)
        frame3 = Frame(self) 
        frame3.grid(row=0, column=3, rowspan=14, columnspan=3, sticky=N + S + W + E)
        entryText = "Input File Name"
        self.text_in = Entry(frame3)
        self.text_in.config(fg="black")
        self.text_in.insert(0, entryText)
        self.text_in.pack(side="top", fill='both', expand=1)
        self.text_in2 = Text(frame3)
        self.text_in2.pack(side='left', fill='both', expand=1)
root = Tk()
app = Application(master=root)                
app.mainloop()
