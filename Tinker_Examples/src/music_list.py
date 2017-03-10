'''
Created on Mar 7, 2017

@author: rduvalwa2
'''

from tkinter import *
#from Music_Get_Functions import musicGet_Functions

class ui_list(Frame):
    def __init__(self, master=None):
        """Main frame initialization (mostly delegated)"""
        Frame.__init__(self, master)
        self.pack()
        self.create_ui_list()

    def create_ui_list(self):
        top = Tk()
        Lb1 = Listbox(top)
        Lb1.insert(1, "Python")
        Lb1.insert(2, "Perl")
        Lb1.insert(3, "C")
        Lb1.insert(4, "PHP")
        Lb1.insert(5, "JSP")
        Lb1.insert(6, "Ruby")
        Lb1.pack()
#        top.mainloop()  
    
class Application(Frame):
    def create_getArtist(self):
#        getArtist_UI(self)
        pass
    def create_getAlbum(self):
#        getAlbum_UI(self)
        pass
    def create_getSong(self):
#        getSong_UI(self)
        pass
    def create_getById(self):
#        getById_UI(self)
        pass
    def create_widgets(self):    
        pass
    
root = Tk()
app = Application(master=root)
app.mainloop()  
