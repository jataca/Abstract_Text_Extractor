# coding: utf-8
from InstrumentType import *
import sys
#from Main import *

#a = InstrumentType()
#b = Lien()

# VARIABLES
instrumentList = [] # array of InstrumentTypes to use
#isInstrument = False # grabbing Lien data
isLien = False
isMortgage = False
isData = False
isClaiment = False
isDate = False
isAmount = False
isBatch = False
isDocID = False
lineCount = 0 # we use this to know when we need to grab data from the file for a new InstrumentType
isClaimentAddress = False
isMortgageeAddress = False
abstractID = str(sys.argv[1]) # IMPORTANT! used to differentiate different abstract requests

dpi = 300

while dpi < 401:
    print "new file"
    filename = abstractID + "-" + str(dpi) + "final.txt"
#openFile = open('300finalNoSpace.txt', 'r')

    openFile = open(filename, 'r')
    '''BEGIN OF TXT FILE PARSING'''
    for line in openFile.readlines(): # line = current file line

        #we need to separate different if statements into new functions and classes. But Python doesn't pass by referece!

        #Check if we have a new Lien
        #if (isLien == False) and (line == "NOTICE OF CLAIM 0F LIEN\n" or line == "NOTICE OF CLAIM OF LIEN\n" or line == "_ NOTICE 0F_CLAIM 0F LIEN\n" or line == "_ NOTICE CFC—LAIM 0F LIEN\n"):
        if (isLien == False) and ("NOTICE" in line or "N0TICE" in line or ("LIEN" in line and "tice" in line) or ("NO" in line and "LIEN" in line)):
            newLien = Lien()
            instrumentList.append(newLien)
            isLien = True # used to be isLien
            lineCount = 0
            isData = True
            print "new Lien"

        #Check if we have a new Mortgage
        if (isMortgage == False) and (line == "PREFERRED MORTGAGE\n" or line == "PREFERRED M0RTGAGE\n"):
            newMortgage = Mortgage()
            instrumentList.append(newMortgage)
            isMortgage = True
            lineCount = 0
            isData = True
            print "new mortgage"

        # grab Instrument data
        if (isLien == True or isMortgage == True) and lineCount == 2 and isData == True:
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
            print "found lien address"
            isClaimentAddress = True
            lineCount = 0

        # Grab mortgagee address
        if isMortgage == True and (line == "MORTGAGEE\n" or line == "M0RTGAGEE\n" or line == "MORTGAG EE\n" or line == "MORTGAG?\n" or line == "M0RTGAGF\n" or line == "M0RTGAG EE\n" or line == "M0RTGAG?\n" or line == "M0RTGAGF\n"):
            print "found mortgage address"
            isMortgageeAddress = True
            lineCount = 0

        # If we passed the last line (just in case we don't capture the state in the last line of the address)
        if (isClaimentAddress == True or isMortgageeAddress == True) and ("PER NOTICE" in line or "LIEN" in line or "INSTRUMENT " in line or "INSTRUHENT " in line
            or " ISSUED " in line or " ABSTRACT " in line or "This space " in line or "PREVIOUS" in line or "EDITION" in line or "..." in line or len(line) < 2):
            isLien = False #no more Lien stuff at this point
            isClaimentAddress = False
            isMortgage = False
            isMortgageeAddress = False

        # add line as part of the Lien's address
        if (isLien == True and lineCount > 0 and isClaimentAddress == True):
            newLien.address += line #append to Lien address

        # add line as part of the Mortgagee's address
        if (isMortgage == True and lineCount > 0 and isMortgageeAddress == True):
            newMortgage.address += line #append to Lien address
            print line

        # if at last line of the address
        if (isClaimentAddress == True or isMortgageeAddress == True) and (" AK " in line or " WA " in line or " CA " in line):
            isLien = False #no more Lien stuff at this point
            isMortgage = False
            isClaimentAddress = False
            isMortgageeAddress = False

        lineCount += 1
        #print isMortgagee
    openFile.close()

    # WRITE RESULTING ADDRESSES TO FILES
    addressFile = "Addresses" + filename
    writeFile = open(addressFile, 'w')
    i = 0
    while i < len(instrumentList):
        writeFile.write(instrumentList[i].address)
        writeFile.write("\n")
        i += 1
    writeFile.close()
    instrumentList = []
    dpi += 25

'''END OF TXT FILE PARSING'''

# How big is our list?
print len(instrumentList)
#print newLien.claiment

i = 0
while i < len(instrumentList):
    print "CLAIMENT: ", i
    #print instrumentList[i].address
    i += 1


#AVERAGEADDRESSES.PY START'S HERE **********************************************



# COUNT THE LINES FOR EACH FILE ************************************************
dpi = 300
numLines = [0, 0, 0, 0, 0]
filenumber = 0
while dpi < 401:
    filename = "Addresses" + abstractID + "-" +  str(dpi) + "final.txt"
    with open(filename) as f:
        for num in enumerate(f): # can we get rid of the l?
            #print i
            pass
    numlines[filenumber] = num
    dpi += 25
    filenumber += 1
    f.close()

# COMPARE NUMBER OF LINES ******************************************************
score = [0, 0, 0, 0, 0] # The higher the score, the more lines are the same. For example, if all the files have the same number they will all be 5
for i in range(len(numLines)):
    for j in range(len(numLines)):
        if numLines[i] != numLines[j]:
            score[i] += 1

# TAKE THE ONE WITH THE HIGHEST SCORE ******************************************
highScore = 0 # indexes with the most frequent line number
highScoreIndex = 0
for i in range(len(score)):
    if score[i] > highScore:
        highScore = score[i]
        highScoreIndex = i

# COMPARE TEXT WITHIN THE MOST FREQUENT ADDRESS FILES AND DISCORD THE OTHERS ***



# CREATE THE TEXT MATRIX
width, height = numLines[highScoreIndex] + 1, 5
TextMatrix = [[0 for x in range(width)] for y in range(height)]

# CREATE THE INTEGER (SCORE) MATRIX
width, height = numLines[highScoreIndex] + 1, 5
IntMatrix = [[0 for x in range(width)] for y in range(height)]

# FILL THE TEXT MATRIX FROM THE RESULTING ADDRESSES*****************************
dpi = 300
filenum = 0
for i in range(len(numLines)):
    if score[i] == highScore:
        dpiAdjuster = 25 * i
        dpi += dpiAdjuster
        fname = "Addresses" + abstractID + "-" +  str(dpi) + "final.txt"
        openFile = open(fname, 'r') # used to be fname
        linenum = 0
        for line in openFile.readlines():
            TextMatrix[filenum][linenum] = line
            linenum+=1
        openFile.close()
        filenum += 1

#INITIALIZE INTMATRIX TO 0
for i in range(0, filenum):
    for j in range(0, linenum):
        IntMatrix[i][j] = 0

#COMPARE MATRIX
for f in range (0, filenum):
    for line in range(0, linenum):
        for file in range (0, filenum):
            if TextMatrix[f][line] == TextMatrix[file][line]:
                IntMatrix[f][line] += 1
            pass



print TextMatrix[0][1]
print "[1, 2, 3, 4, 5, 6, 7, 8, 9, 0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 0, 1, 2, 3, 4, 6, 7, 8]"
print IntMatrix[0]
print IntMatrix[1]
print IntMatrix[2]
print IntMatrix[3]
print IntMatrix[4]
