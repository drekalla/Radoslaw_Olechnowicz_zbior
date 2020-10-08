# -*- coding: utf-8 -*-
"""
Created on Sun Apr 26 11:51:51 2020

@author: Radosław Olechnowicz
"""
from tkinter import *
from PIL import ImageTk, Image
from pynput.keyboard import Key, Controller
import tkinter.messagebox
import os
import time
#import ARM_Tv1


class start_window(Frame):
    def __init__(self, parent=None):
        Frame.__init__(self, parent)
        Frame.pack(self)
        Label(self, text = 'Test', width=30).pack()


if __name__ == '__main__':

    root = Tk()
    root.title("ARM-T")
    root.geometry("350x220")
    root.iconbitmap('logo.ico')
    
    my_img = ImageTk.PhotoImage(Image.open("tibialogo.png"))
    
    running = False
    mushroom = False
    heal = False
    life = False
    soft = False
    clock = 0
    
    def run():
        if running:
            global clock
            keyboard = Controller()
            if(clock==0):
                time.sleep(2)
                keyboard.press('l')
                keyboard.release('l')
                time.sleep(0.2)
                
                for x in range(4):
                    keyboard.press('m')
                    keyboard.release('m')
                    time.sleep(0.2)
                
                keyboard.press('h')
                keyboard.release('h')
                time.sleep(0.2)
                
                keyboard.press('s')
                keyboard.release('s')
                time.sleep(0.2)
                
            clock= clock+1
            keyboard.press('a')
            keyboard.release('a')
            
            if(clock%260==0):
                if mushroom:
                    keyboard.press('m')
                    keyboard.release('m')
                
            if(clock%450==0):
                if heal:
                    keyboard.press('h')
                    keyboard.release('h')
                
            if(clock%1200==0):
                if life:
                    keyboard.press('l')
                    keyboard.release('l')
            
            if (clock%14401==0):
                if soft:
                    keyboard.press('s')
                    keyboard.release('s')
                clock=0
                
            print(clock)
        root.after(1000, run)
            
    
    def callback1():
        a.configure(bg = "green")
        b.configure(bg = "white")
        logolabel.configure(bg = "green")
        timelabel.configure(text="Work")
        #ARM_Tv1.run(1)
        global clock
        global running
        clock = 0
        running = True
        print("Start!")
        
    
    def callback2():
        a.config(bg = "white")
        b.config(bg = "red")
        logolabel.configure(bg = "red")
        timelabel.configure(text="Not Work")
        #ARM_Tv1.run(0)
        global running
        running = False
        print("Stop!")
        

    #f = Frame(root, height=32, width=64)
    #f.pack_propagate(0)

    
    a = Button(root,
               text="Start",
               bg = "white",
               width=5,
               height=2,
               command=callback1)
    
    b = Button(root,
               text="Stop",
               bg = "white",
               width=5,
               height=2,
               command=callback2)
    
    logolabel = Label(image = my_img,
                      bg = "white")
    
    timelabel = Label(text="")
    

    
    thelabel = Label(root,
                     text="ARM-T \n Auto Rune Maker - Tibia")



    #f.pack()
    a.pack(side=LEFT)
    b.pack(side=RIGHT)
    thelabel.pack(side=TOP)
    logolabel.pack(side=TOP)
    timelabel.pack(side=BOTTOM)

    root.after(100, run)
    root.mainloop()
