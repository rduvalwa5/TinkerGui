'''

Created on Mar 7, 2017
https://www.tutorialspoint.com/python/tk_listbox.htm
@author: rduvalwa2
'''
from tkinter import *
#import tkMessageBox
#import Tkinter

top = Tk()

songs = [('Song l','Album 1'),('Song 2','Album 2'),('Song 3','Album 3')]


Lb1 = Listbox(top)
num = 0
for num in range(len(songs)):
    Lb1.insert(num, songs[num][0] +'\t' + songs[num][1])
    print(num, songs[num])

Lb1.pack()
top.mainloop()