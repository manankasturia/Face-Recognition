import cv2 as cv
import numpy as np

img = cv.imread('pictures/cats.jpg')
cv.imshow("Original", img)

blank = np.zeros(img.shape, dtype='uint8')
cv.imshow("Blank", blank)

# Canny way of finding contours

# Original image countours
canny = cv.Canny(img, 125, 175)
cv.imshow("Canny", canny)

contours1, hierarchies1 = cv.findContours(canny, cv.RETR_LIST, cv.CHAIN_APPROX_SIMPLE)
print(f"{len(contours1)} contours found in original canny way")

# Blurred image contours
blur = cv.blur(img, (3,3), cv.BORDER_DEFAULT)
cv.imshow("Blurred", blur)

cannyBlur = cv.Canny(blur, 125, 175)
cv.imshow("CannyBlur", cannyBlur)

contours2, hierarchies2 = cv.findContours(cannyBlur, cv.RETR_LIST, cv.CHAIN_APPROX_SIMPLE)
print(f"{len(contours2)} contours found in blur canny way")

# threshold way of finding contours

gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)

ret, thresh = cv.threshold(gray, 125, 255, cv.THRESH_BINARY)
# threshold binarizes an image if image pixel intensity is less than 125 it will be set to 0 else it will be set to 1
cv.imshow("Threshold", thresh)

contours3, hierarchies3 = cv.findContours(thresh, cv.RETR_LIST, cv.CHAIN_APPROX_SIMPLE)
print(f"{len(contours3)} contours found in original(gray) threshold way")

cv.drawContours(blank, contours3, -1, (0,0,255), 1) # -1 specifies that we want to draw all contours
cv.imshow("Contours Drawn(Threshold)", blank)

# therefore contours are like boundaries in the image

cv.waitKey(0)