#!/usr/bin/python

import Tkinter
from Tkinter import *
import tkMessageBox
from tkFileDialog import askopenfilename


root = Tkinter.Tk()
# Code to add widgets will go here...

#set size of window
root.geometry("500x500")

def pageSelectors(string):
    firstVar = StringVar()
    firstLabel = Label( root, textvariable=firstVar )
    firstVar.set("First Page:")
    firstLabel.pack()
    firstPage = Spinbox(root, from_=0, to=10)
    firstPage.pack()

    lastVar = StringVar()
    lastLabel = Label( root, textvariable=lastVar )
    lastVar.set("Last Page:")
    lastLabel.pack()
    lastPage = Spinbox(root, from_=0, to=10)
    lastPage.pack()

    parseButton = Tkinter.Button(root, text="Get Addresses")
    parseButton.pack()

# Function for button
def helloCallBack():
   #tkMessageBox.showinfo( "Hello Python", "Hello World")
   filepath = askopenfilename() # show an "Open" dialog box and return the path to the selected file
   filename = StringVar()
   filelabel = Label( root, textvariable=filename)
   filename.set(filepath)
   filelabel.pack()
   pageSelectors("hello")

# Text Label
var = StringVar()
label = Label( root, textvariable=var )
var.set("Abstract Parser")
label.pack()

#Button
testButton = Tkinter.Button(root, text ="Select Abstract (pdf)", command = helloCallBack)
testButton.pack()


#start program
root.mainloop()
