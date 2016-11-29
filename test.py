import sys

dpi = 300
filename = str(dpi) + "final.txt"

print dpi
print filename


if len(sys.argv) > 0:
    abstractID = str(sys.argv[1])

print abstractID
