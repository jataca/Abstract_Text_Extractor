from InstrumentType import *
#from Main import *

#a = InstrumentType()
#b = Lien()

# VARIABLES
instrumentList = [] # array of InstrumentTypes to use
isLien = False # grabbing Lien data
isData = False
isClaiment = False
isDate = False
isAmount = False
isBatch = False
isDocID = False
lineCount = 0 # we use this to know when we need to grab data from the file for a new InstrumentType

#open the file

openFile = open('300final.txt', 'r')

'''BEGIN OF TXT FILE PARSING'''
for line in openFile.readlines(): # line = current file line

    #we need to separate different if statements into new functions and classes. But Python doesn't pass by referece!

    #If we find a new Lien
    if line == "NOTICE OF CLAIM 0F LIEN\n" or line == "NOTICE OF CLAIM OF LIEN\n":
        newLien = Lien()
        instrumentList.append(newLien)
        isLien = True
        lineCount = 0
        #print line
        isData = True

    # grab Lien data
    if (isLien == True and lineCount == 2 and isData == True):
        isConveyed = True
        # print line
        for character in line:
            if (isConveyed == True):
                pass
            if (isDate == True):
                pass
            if (isAmount == True):
                pass
            if (isBatch == True):
                pass
            if (isDocID == True):
                pass
        isData = False

    # Grab Lien Claimant address information
    if (isLien == True and line == "CLAIMANT\n"):
        isClaiment = True
        lineCount = 0

    if ("PER NOTICE OF CLAIM OF LIEN" in line):
        isLien = False #no more Lien stuff at this point

    if (isLien == True and lineCount > 0 and isClaiment == True):
        newLien.claiment += line #append to Lien address

    lineCount += 1

'''END OF TXT FILE PARSING'''

# How big is our list?
print len(instrumentList)
#print newLien.claiment
#print instrumentList[0].claiment
