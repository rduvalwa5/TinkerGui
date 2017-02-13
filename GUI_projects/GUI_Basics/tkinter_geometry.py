from tkinter import *

root = Tk()
frame = Frame(root)
frame.pack()

bottomframe = Frame(root,bg='red')
topframe = Frame(root)
bottomframe.pack( side = BOTTOM )
topframe.pack(side = TOP)

topbutton = Button(topframe, text="Top", fg="black",bg="red")
topbutton.pack(side = TOP)

redbutton = Button(frame, text="Red", fg="red")
redbutton.pack( side = LEFT)

greenbutton = Button(frame, text="Brown", fg="brown")
greenbutton.pack( side = LEFT )

bluebutton = Button(frame, text="Blue", fg="blue")
bluebutton.pack( side = LEFT )

blackbutton = Button(bottomframe, text="Black", fg="black")
blackbutton.pack( side = BOTTOM)


root.mainloop()
