import socket
import Tkinter
from Tkinter import *
import tkMessageBox
from tkFileDialog import askopenfilename


root = Tkinter.Tk()
# Code to add widgets will go here...

#set size of window
root.geometry("500x500")

#Global file Name
fileNameList = ["empty"]
print(fileNameList[0])


# Function for button
def helloCallBack(fileNameList):
   #tkMessageBox.showinfo( "Hello Python", "Hello World")
   filepath = askopenfilename() # show an "Open" dialog box and return the path to the selected file
   filename = StringVar()
   filelabel = Label( root, textvariable=filename)
   filename.set(filepath)
   filelabel.pack()
   fileNameList[0] = filepath

def sendPDF(fileNameList):
    if (fileNameList[0] == "empty"):
        pass
    else:
        # Create a TCP/IP socket
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

        # Connect the socket to the port where the server is listening
        server_address = ('192.168.1.24', 6789)
        print >>sys.stderr, 'connecting to %s port %s' % server_address
        sock.connect(server_address)


        try:
            '''
            # Send data
            message = 'This is the message.  It will be repeated.'
            print >>sys.stderr, 'sending "%s"' % message
            sock.sendall(message)

            # Look for the response
            amount_received = 0
            amount_expected = len(message)

            while amount_received < amount_expected:
                data = sock.recv(64)
                amount_received += len(data)
                print >>sys.stderr, 'received "%s"' % data
                var = StringVar()
                label = Label( root, textvariable=var )
                var.set("PDF RECIEVED SUCCESSFULLY") # put this in an if statement to make sure
                label.pack()

            # Try sending a file in 1024 byte chunks
            fileOpen = open(fileNameList[0], 'r')
            print 'Sending...'
            fileRead = fileOpen.read(1024)
            while (fileRead):
                print 'Sending...'
                fileSend.send(fileRead)
                fileRead = fileOpen.read(1024)
'''
            fileOpen = open(fileNameList[0], 'r')
            print 'Sending...'
            fileRead = fileOpen.read(1024)
            while (fileRead):
                print 'Sending...'
                sock.send(fileRead)
                fileRead = fileOpen.read(1024)

            # Try this to see if we can send the entire pdf at once
            #sock.sendall(fileOpen) # can only send a string in sendall()



        finally:
            print >>sys.stderr, 'closing socket'
            sock.close()

# Text Label
var = StringVar()
label = Label( root, textvariable=var )
var.set("Abstract Parser")
label.pack()

#Button
testButton = Tkinter.Button(root, text ="Select Abstract (pdf)", command = lambda : helloCallBack(fileNameList))
testButton.pack()

# first page
firstVar = StringVar()
firstLabel = Label( root, textvariable=firstVar )
firstVar.set("First Page:")
firstLabel.pack()
firstPage = Spinbox(root, from_=0, to=10)
firstPage.pack()

#last page
lastVar = StringVar()
lastLabel = Label( root, textvariable=lastVar )
lastVar.set("Last Page:")
lastLabel.pack()
lastPage = Spinbox(root, from_=0, to=10)
lastPage.pack()

#send pdf to server
parseButton = Tkinter.Button(root, text="sendPDF", command = lambda : sendPDF(fileNameList))
parseButton.pack()

#start program
root.mainloop()
