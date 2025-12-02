import cv2 as cv

img = cv.imread('pictures/cats.jpg')
cv.imshow("Original", img)

gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
cv.imshow("Grayscale", gray)

# Simple Thresholding - sets each pixels greater than second parameter to the value in third parameter
threshold, thresh = cv.threshold(gray, 150, 255, cv.THRESH_BINARY)
cv.imshow("Simple Thresholding", thresh)

threshold, thresh_inv = cv.threshold(gray, 150, 255, cv.THRESH_BINARY_INV)
cv.imshow("Simple Thresholding Inverse", thresh_inv)

# Adaptive Thresholding - it finds the optimal thresholding value by itself so we don't need to specify value like 150
adaptive_thresh = cv.adaptiveThreshold(gray, 255, cv.ADAPTIVE_THRESH_MEAN_C, cv.THRESH_BINARY, 11, 3)
# 11 is the blocksize(kernel value) which opencv takes to find mean around that many pixels to compute optimal thresholding value
# 3 is C value which is subtracted from mean to fine tune threshold
cv.imshow("Adaptive Thresholding", adaptive_thresh)

cv.waitKey(0)