#!/usr/bin/python

import Tkinter
from Tkinter import *
import tkMessageBox
from tkFileDialog import askopenfilename


root = Tkinter.Tk()
# Code to add widgets will go here...

#set size of window
root.geometry("500x500")

# Function for button
def helloCallBack():
   #tkMessageBox.showinfo( "Hello Python", "Hello World")
   filename = askopenfilename() # show an "Open" dialog box and return the path to the selected file


# Text Label
var = StringVar()
label = Label( root, textvariable=var )
var.set("Abstract Parser")
label.pack()

#Button
testButton = Tkinter.Button(root, text ="Hello", command = helloCallBack)
testButton.pack()


#start program
root.mainloop()
