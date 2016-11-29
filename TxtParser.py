from InstrumentType import *
#from Main import *

#a = InstrumentType()
#b = Lien()

# VARIABLES
instrumentList = [] # array of InstrumentTypes to use
isInstrument = False # grabbing Lien data
isData = False
isClaiment = False
isDate = False
isAmount = False
isBatch = False
isDocID = False
lineCount = 0 # we use this to know when we need to grab data from the file for a new InstrumentType
isClaimentAddress = False
isMortgageeAddress = False

dpi = 300

while dpi < 401:
    print "round"
    filename = str(dpi) + "finalNoSpace.txt"
#openFile = open('300finalNoSpace.txt', 'r')

    openFile = open(filename, 'r')
    '''BEGIN OF TXT FILE PARSING'''
    for line in openFile.readlines(): # line = current file line

        #we need to separate different if statements into new functions and classes. But Python doesn't pass by referece!

        #Check if we have a new Lien
        if line == "NOTICE OF CLAIM 0F LIEN\n" or line == "NOTICE OF CLAIM OF LIEN\n":
            newLien = Lien()
            instrumentList.append(newLien)
            isInstrument = True # used to be isLien
            lineCount = 0
            isData = True
            #isClaimentAddress = False

        #Check if we have a new Mortgage
        if line == "PREFERRED MORTGAGE\n" or line == "PREFERRED M0RTGAGE\n":
            newMortgage = Mortgage()
            instrumentList.append(newMortgage)
            isInstrument = True
            lineCount = 0
            isData = True

        # grab Instrument data
        if (isInstrument == True and lineCount == 2 and isData == True):
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
        if (isInstrument == True and line == "CLAIMANT\n"):
            isClaimentAddress = True
            lineCount = 0

        if isInstrument == True and (line == "MORTGAGEE\n" or line == "M0RTGAGEE"):
            isMortgageeAddress = True
            lineCount = 0

        # If we passed the last line (by using states we can probably delete this one)
        if ("PER NOTICE OF CLAIM OF LIEN" in line or "PER NOTICE OF CLAIM 0F LIEN" in line or "PER NOTTCE OF CLAIM OF IJEN" in line or "PER NOTTCE OF CLAIM OF LIEN" in line):
            isInstrument = False #no more Lien stuff at this point
            isClaimentAddress = False

        if (isInstrument == True and lineCount > 0 and isClaimentAddress == True):
            newLien.address += line #append to Lien address

        if (isInstrument == True and lineCount > 0 and isMortgageeAddress == True):
            newMortgage.address += line #append to Lien address

        # if at last line of the address
        if (" AK " in line or " WA " in line):
            isInstrument = False #no more Lien stuff at this point
            isClaimentAddress = False
            isMortgageeAddress = False

        lineCount += 1
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
    print instrumentList[i].address
    i += 1


#print instrumentList[0].claiment
