'''
Instructions:
 1.  Write a GUI-based program that provides:
       two Entry fields,
       a button 
       and a label.
 2.  When the button is clicked, the value of each Entry should (if possible) be converted into a float. 
 3.  If both conversions succeed, the label should change to the sum of the two numbers. Otherwise it should read "***ERROR***".
@author: rduval
'''

from tkinter import *
# from decimal import *

class Application(Frame):
    """Application main window class."""
    
    
    def __init__(self, master=None):
        """Main frame initialization (mostly delegated)"""
        Frame.__init__(self, master)
        self.pack()
        self.createWidgets()

    def createWidgets(self):
        self.input1_frame = Frame(self)
        self.text_in_one = Entry(self.input1_frame)
        self.text_in_one.pack(side=RIGHT)
        self.label = Label(self.input1_frame, text="Input 1: ")
        self.label.pack(side=LEFT)
        self.input1_frame.pack()

        self.input2_frame = Frame(self)
        self.text_in_two = Entry(self.input2_frame)
        self.text_in_two.pack(side=RIGHT)
        self.label = Label(self.input2_frame, text="Input 2: ")
        self.label.pack(side=LEFT)
        self.input2_frame.pack()
        
        self.result_frame = Frame(self)
        self.result = Label(self.result_frame, text="Result")
        self.result.pack(side=TOP)
        self.result_frame.pack()

        self.button_frame = Frame(self)
        self.QUIT = Button(self.button_frame, text="Quit", command=self.quit, state='active')
        self.QUIT.pack(side=LEFT)
        self.handleb = Button(self.button_frame, text="Compute", command=self.handle)
        self.handleb.pack(side=RIGHT)
        self.button_frame.pack()
        
        
    def handle(self):
        def is_number(s):
            try:
                float(s)
                return True
            except ValueError:
                return False
            
        text1 = self.text_in_one.get()
        text2 = self.text_in_two.get()
        print(text1)
        print(text2)
        
        if is_number(text1) == True & is_number(text2) == True:
                total = float(text1) + float(text2)
                print(total)
                self.result.config(text=total)  
        else:
            self.result.config(text="***ERROR***")
    
root = Tk()
app = Application(master=root)
app.mainloop()  
    
