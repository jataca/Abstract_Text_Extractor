#!/bin/bash

gs -sDEVICE=tiff48nc -dNOPAUSE -dBATCH -dTextAlphaBits=4 -dGraphicsAlphaBits=4 -dDOINTERPOLATE -dDISKFONTS -r300 -o 300final.tiff ocean_cape_abstract.pdf

tesseract 300final.tiff 300final

grep -v '^$' 300final.txt > 300finalNoSpace.txt
