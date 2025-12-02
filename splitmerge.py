import cv2 as cv
import numpy as np

img = cv.imread('pictures/park.jpg')
cv.imshow("Original", img)

blank = np.zeros(img.shape[:2], dtype='uint8')

b,g,r = cv.split(img)

# it would display white where color intensity of that particular is more and black where it is less
cv.imshow('Blue', b)
cv.imshow('Green', g)
cv.imshow('Red', r)

print("Original: ", img.shape) # 3 represents 3 color channels
# no color channel specified means there is just 1 color channel
print("Blue: ", b.shape)
print("Green: ", g.shape)
print("Red", r.shape)

merged = cv.merge([b,g,r])
cv.imshow("Merged Image", merged)

# To show blue in splitted blue image and same for green and red we can do this
# we are basically showing black for the colors that are not in image to make it 3 color channels so we can display it in color
blue = cv.merge([b,blank,blank])
green = cv.merge([blank,g,blank])
red = cv.merge([blank,blank,r])

cv.imshow('Blue blank merged', blue)
cv.imshow('Green blank merged', green)
cv.imshow('Red blank merged', red)

cv.waitKey(0)