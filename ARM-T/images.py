# -*- coding: utf-8 -*-
"""
Created on Mon Apr 27 12:12:35 2020

@author: Radek
"""

import time
from tkinter import *
def changeTitle(root, val, t):
    root.title(val)
    root.after(1000, lambda:countdown(t-1, root))
def countdown(t, root):
    if t+1:
        mins, secs = divmod(t, 60)
        timeformat = "{:02d}:{:02d}".format(mins, secs)
        changeTitle(root, timeformat, t)
    else:
        return
root=Tk()
countdown(2, root)
mainloop()