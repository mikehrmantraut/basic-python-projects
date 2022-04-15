""" 
Digital Clock with Python
Tkinter is a Python binding to the Tk GUI toolkit. 
It is the standard Python interface to the Tk GUI toolkit, and is Python's de facto standard GUI.
Tkinter is included with standard Linux, Microsoft Windows and Mac OS X installs of Python.
If you do not have this module, write 'pip install tk' to terminal.
author: Mehmet Baran Munar
"""

from tkinter import Tk, Label, mainloop
import datetime
from time import strftime

root = Tk()
root.title('Clock')

def clock():
    text = strftime('%H:%M:%S')
    label.config(text=text)
    label.after(1000, clock)

label = Label(root, font=("Freestyle Script", 100), background='black', foreground='white')
label.pack(anchor='center')

clock()
mainloop()
