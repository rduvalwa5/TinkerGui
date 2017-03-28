'''
        "arrow"
        "circle"
        "clock"
        "cross"
        "dotbox"
        "exchange"
        "fleur"
        "heart"
        "heart"
        "man"
        "mouse"
        "pirate"
        "plus"
        "shuttle"
        "sizing"
        "spider"
        "spraycan"
        "star"
        "target"
        "tcross"
        "trek"
        "watch"
'''



from tkinter import *
import tkinter

top = tkinter.Tk()

B1 = tkinter.Button(top, text="circle", relief=RAISED, \
                         cursor="circle")
B2 = tkinter.Button(top, text="plus", relief=RAISED, \
                         cursor="plus")
B3 = tkinter.Button(top, text="man", relief=RAISED, \
                         cursor="man")
B4 = tkinter.Button(top, text="pirate", relief=RAISED, \
                         cursor="pirate")
B5 = tkinter.Button(top, text="shuttle", relief=RAISED, \
                         cursor="shuttle")
B6 = tkinter.Button(top, text="spider", relief=RAISED, \
                         cursor="spider")
B7 = tkinter.Button(top, text="spraycan", relief=RAISED, \
                         cursor="spraycan")
B8 = tkinter.Button(top, text="fleur", relief=RAISED, \
                         cursor="fleur")

B1.pack()
B2.pack()
B3.pack()
B4.pack()
B5.pack()
B6.pack()
B7.pack()
B8.pack()
top.mainloop()
