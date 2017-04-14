'''
https://pythonspot.com/en/tk-file-dialogs/
https://www.safaribooksonline.com/library/view/python-cookbook/0596001673/ch09s04.html
http://www.python-course.eu/tkinter_dialogs.php

from tkinter import filedialog
from tkinter import *
 
root = Tk()
root.filename =  filedialog.askopenfilename(initialdir = "/",title = "Select file",filetypes = (("jpeg files","*.jpg"),("all files","*.*")))
print (root.filename)
'''
from tkinter import *
from tkinter import filedialog      

def callback():
    name= filedialog.askopenfilename() 
    print(name)
    
errmsg = 'Error!'
Button(text='File Open', command=callback).pack(fill=X)
mainloop()