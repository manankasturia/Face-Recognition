import cv2 as cv

img = cv.imread('pictures/park.jpg')
cv.imshow("Original", img)

# BGR to grayscale
gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
cv.imshow("Grayscale", gray)

# BGR to HSV
hsv = cv.cvtColor(img, cv.COLOR_BGR2HSV)
cv.imshow("HSV", hsv)

# BGR to L*a*b
lab = cv.cvtColor(img, cv.COLOR_BGR2LAB)
cv.imshow("LAB", lab)

# BGR to RGB
rgb = cv.cvtColor(img, cv.COLOR_BGR2RGB)
cv.imshow('RGB', rgb)
# as opencv can only display bgr images so when we try to display rgb image it shows red as blue and blue as red

# HSV to BGR
hsv2bgr = cv.cvtColor(hsv, cv.COLOR_HSV2BGR)
cv.imshow("HSV to BGR", hsv2bgr)

# LAB to BGR
lab2bgr = cv.cvtColor(lab, cv.COLOR_LAB2BGR)
cv.imshow("LAB to BGR", lab2bgr)

cv.waitKey(0)