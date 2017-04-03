'''
Created on Mar 26, 2017

@author: rduvalwa2
'''
from tkinter import *

root = Tk()
scrollbar = Scrollbar(root)
scrollbarh = Scrollbar(root,orient=HORIZONTAL,width=10)
scrollbar.pack( side = RIGHT, fill=Y)
scrollbarh.pack(side = BOTTOM, fill=X)
#self.xscrollbar = Scrollbar(self.root, orient=HORIZONTAL, command=self.canvas.xview)
mylist = Listbox(root, yscrollcommand = scrollbar.set, xscrollcommand = scrollbarh.set,bd = 6, bg = 'green' ,width = 100)

for line in range(100):
   mylist.insert(END, "This is line number " + str(line))

mylist.pack( side = LEFT, fill = BOTH )
scrollbar.config( command = mylist.yview)
scrollbarh.config(command = mylist.xview)
mainloop()