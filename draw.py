import cv2 as cv
import numpy as np

               # (height, width, color channels)
blank = np.zeros((500, 500, 3), dtype='uint8') # uint8 is datatype of an image
cv.imshow('Blank', blank)

# paint image with a color
blank[:] = 255,0,0 # B,G,R
cv.imshow('Blue', blank)

# paint a certain  portion of the image
blank[200:300, 300:400] = 0,255,0 # [range of height, range of width]
cv.imshow('Portion', blank)

# draw a line
cv.line(blank, (0,250), (500,250), (255,255,255), thickness = 4)
cv.imshow('Line', blank)

# draw a rectangle
cv.rectangle(blank, (0,0), (250,250), (0,0,255), thickness=-1) # thickness refers to border thickness, -1 and cv.FILLED will fill it
cv.imshow('Rectangle', blank)

# draw a circle
cv.circle(blank, (blank.shape[1]//2, blank.shape[0]//2), 40, (0,0,0), thickness = 2)
cv.imshow('Circle', blank)

# write text
cv.putText(blank, "Hello", (100, 400), cv.FONT_HERSHEY_TRIPLEX, 1.0, (0,0,0), 2)
cv.imshow('Text', blank)

cv.waitKey(0)