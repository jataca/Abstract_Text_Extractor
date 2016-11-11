#Ghostscript
#Links: http://www.ghostscript.com/doc/current/Devices.htm#PNG
# Definitions:
#   1. Bit depth: Bit depth refers to the color information stored in an image. The higher the bit depth of an image, the more colors it can store. The simplest image, a 1 bit image, can only show two colors, black and white.


# Parameters:
#   1. -sDEVICE=pnggray: The output device. For PNGs we use pnggray.
#   2. -q: Quiet startup: suppress normal startup messages, and also do the equivalent of -dQUIET.
#   3. -dTextAlphaBits=n: The subsampling box size n should be 4 for optimum output
#   4. -dGraphicsAlphaBits=n: The subsampling box size n should be 4 for optimum output
#   5. -dDOINTERPOLATE: Turns on image interpolation for all images, improving image quality for scaled images at the expense of speed.
#  *6. -dDITHERPPI=lpi: Forces all devices to be considered high-resolution, and forces use of a halftone screen or screens with lpi lines per inch, disregarding the actual device resolution. Reasonable values for lpi are N/5 to N/20, where N is the resolution in dots per inch.
#   7. -dDISKFONTS: Causes individual character outlines to be loaded from the disk the first time they are encountered.
#   8. -rXRESxYRES (or -r): Output resolution. (Screenshot of pdf page was 946 × 1216, not sure if that's helpful in anyway)


# -o outputname.png ocean_cape_abstract.pdf[0]


1. gs -sDEVICE=pnggray -q -dTextAlphaBits=4 -dGraphicsAlphaBits=4 -dDOINTERPOLATE -dDISKFONTS -r300 -dFirstPage=1 -dLastPage=1 -o page1_dpi300.png ocean_cape_abstract.pdf
    #Result: Very good for pages 1 and 2. Very few errors with -r300

2. gs -sDEVICE=pnggray -q -dTextAlphaBits=4 -dGraphicsAlphaBits=4 -dDOINTERPOLATE -dDISKFONTS -r946×1216 -dFirstPage=2 -dLastPage=2 -o Test_ResultsRes.png ocean_cape_abstract.pdf

3. gs -sDEVICE=pnggray -dNOPAUSE -dBATCH -dTextAlphaBits=4 -dGraphicsAlphaBits=4 -dDOINTERPOLATE -dDISKFONTS -r300 -o 300dpi%02d.png ocean_cape_abstract.pdf
    #Result: Creates multiple PNGs. but requires individual tesseract commands which create separate text files
    #tesseract 300dpi01.png 300dpi01
    #tesseract 300dpi02.png 300dpi02
    #tesseract 300dpi03.png 300dpi03
    #tesseract 300dpi04.png 300dpi04
    #tesseract 300dpi05.png 300dpi05
    #tesseract 300dpi06.png 300dpi06


'''THIS IS THE PLACE'''
4. gs -sDEVICE=tiff48nc -dNOPAUSE -dBATCH -dTextAlphaBits=4 -dGraphicsAlphaBits=4 -dDOINTERPOLATE -dDISKFONTS -r300 -o 300final.tiff ocean_cape_abstract.pdf
    #Result: we can get all of the images of the PDF into one png this way and run 1 tesseract command against it.

#ImageMagick
1. convert -density 400% ocean_cape_abstract.pdf[0] page0.png #Result: Some success. But a lot of the result is simply missing.

2. convert -density 400% ocean_cape_abstract.pdf[0] -resize 25%  page0.png #Result: useless

3.


#Try resizing down and then enlarging to see if we can get cleaner text?
    #Result: Awful



#potrace
# potrace is a tool for smoothing edges. Looks like the time we put into it isn't worth it. the results are bleh.
# only bitmap files can be used with potrace. so we must first convert our pdf or image to bitmap.(PBM, PGM, PPM, or BMP)

1. convert -alpha remove Test_Results2-400.png pgm: | mkbitmap -f 32 -t 0.4 - -o - | potrace --svg -o Test_Results2-400.svg
 #Result: decent. nothing to write home about

2. convert -alpha remove ocean_cape_abstract.pdf pgm: | mkbitmap -f 32 -t 0.4 - -o - | potrace --svg -o ocean_cape_abstract.svg
    #Result: AWful

3. convert -alpha remove Test_Results2-400.png pgm: | mkbitmap -f 4 -t 0.4 - -o - | potrace --svg -o Test_Results2-400_f4_t4.svg
    #Result: AWful

4. convert -alpha remove Test_Results2-400.png pgm: | mkbitmap -f 70 -t 0.4 - -o - | potrace --svg -o Test_Results2-400_f70_t4.svg
    #Result: same as -f 32

5. convert -alpha remove Test_Results2-400.png pgm: | mkbitmap -f 32 -t 0.5 - -o - | potrace --svg -o Test_Results2-400_f32_t5.svg
    #Result: Ink is a little more bold than -t 0.4 (-t 0.9 makes the page black)

6. convert -alpha remove Test_Results2-400.png pgm: | mkbitmap -f 32 -t 0.2 - -o - | potrace --svg -o Test_Results2-400_f32_t2.svg


# convertion from svg to png
convert Test_Results2-400.svg lastHope1.png

convert Test_Results2-400_f32_t5.svg Test_Results2-400_f32_t5.png

convert -density 300 Test_Results2-400_f32_t5.svg Test_Results2-400_t5_d300.png
# Legend:
# * = not used for now
