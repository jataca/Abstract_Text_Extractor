
dpi = 300
'''
#COUNT LINES IN CASE THERE IS A DIFFERENCE BETWEEN THE FILES
#while dpi < 401
fname = "Addresses" + str(dpi) + "finalNoSpace.txt"
with open(fname) as f:
    for i, l in enumerate(f):
        print i
'''
#theDic = {}
#addresses = []

filename = "Addresses" + str(dpi) + "finalNoSpace.txt"
# GET THE NUMBER OF LINES OUT OF THE FILE SO WE KNOW HOW BIG TO MAKE THE MATRICES
with open(filename) as f:
    for i, l in enumerate(f):
        print i

f.close()

# CREATE THE TEXT MATRIX
width, height = i + 1, 5
TextMatrix = [[0 for x in range(width)] for y in range(height)]

# CREATE THE INTEGER (SCORE) MATRIX
width, height = i + 1, 5
IntMatrix = [[0 for x in range(width)] for y in range(height)]

# FILL THE TEXT MATRIX FROM THE RESULTING ADDRESSES
filenum = 0
while dpi < 401:
    fname = "Addresses" + str(dpi) + "finalNoSpace.txt"
    openFile = open(fname, 'r')
    linenum = 0
    for line in openFile.readlines():
        TextMatrix[filenum][linenum] = line
        #print j
        linenum+=1
    openFile.close()
    filenum += 1
    dpi += 25

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
