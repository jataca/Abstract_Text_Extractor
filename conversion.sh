#!/bin/bash

abstractID=$1 #Grab the parameter abstract id
abstractPDF=$2

gs -sDEVICE=tiff48nc -dNOPAUSE -dBATCH -dTextAlphaBits=4 -dGraphicsAlphaBits=4 -dDOINTERPOLATE -dDISKFONTS -r300 -o 300final.tiff ocean_cape_abstract.pdf
gs -sDEVICE=tiff48nc -dNOPAUSE -dBATCH -dTextAlphaBits=4 -dGraphicsAlphaBits=4 -dDOINTERPOLATE -dDISKFONTS -r325 -o 325final.tiff ocean_cape_abstract.pdf
gs -sDEVICE=tiff48nc -dNOPAUSE -dBATCH -dTextAlphaBits=4 -dGraphicsAlphaBits=4 -dDOINTERPOLATE -dDISKFONTS -r350 -o 350final.tiff ocean_cape_abstract.pdf
gs -sDEVICE=tiff48nc -dNOPAUSE -dBATCH -dTextAlphaBits=4 -dGraphicsAlphaBits=4 -dDOINTERPOLATE -dDISKFONTS -r375 -o 375final.tiff ocean_cape_abstract.pdf
gs -sDEVICE=tiff48nc -dNOPAUSE -dBATCH -dTextAlphaBits=4 -dGraphicsAlphaBits=4 -dDOINTERPOLATE -dDISKFONTS -r400 -o 400final.tiff ocean_cape_abstract.pdf

tesseract 300final.tiff 300final
tesseract 325final.tiff 325final
tesseract 350final.tiff 350final
tesseract 375final.tiff 375final
tesseract 400final.tiff 400final

grep -v -e '^ *$' 300final.txt > 300finalNoSpace.txt # Remove all lines
grep -v -e '^ *$' 325final.txt > 325finalNoSpace.txt # Remove all lines
grep -v -e '^ *$' 350final.txt > 350finalNoSpace.txt # Remove all lines
grep -v -e '^ *$' 375final.txt > 375finalNoSpace.txt
grep -v -e '^ *$' 400final.txt > 400finalNoSpace.txt # Remove all lines

grep -v -e '^ *$' 3-300.txt > 3-300final.txt
grep -v -e '^ *$' 3-325.txt > 3-325final.txt
grep -v -e '^ *$' 3-350.txt > 3-350final.txt
grep -v -e '^ *$' 3-375.txt > 3-375final.txt
grep -v -e '^ *$' 3-400.txt > 3-400final.txt
