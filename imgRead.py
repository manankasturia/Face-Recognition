import cv2 as cv

img = cv.imread('pictures/cat.jpg') # this image is of low resolution so displaying it wouldn't be a problem(will fit on screen)
cv.imshow('Cat', img)

cv.waitKey(0) # the value inside brackets is wait time in ms, we give value 0 for it to wait indefinitely