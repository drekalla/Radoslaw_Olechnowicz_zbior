# -*- coding: utf-8 -*-
"""
Created on Sun Apr 26 11:36:55 2020

@author: Radosław Olechnowicz
"""
import time
from pynput.keyboard import Key, Controller
import tkinter.messagebox
import Gui_ARM_T


def run(a):
    
    if (a==True):
        keyboard = Controller()
        time.sleep(0.2)
        keyboard.press('a')
        keyboard.release('a')
        Gui_ARM_T.root.after(1000, run)

    elif (a==False):
        return
    else:
        tkinter.messagebox.showerror(title="error",
                                     message="Nieznany Błąd!")
        return
        