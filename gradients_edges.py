import cv2 as cv
import numpy as np

img = cv.imread('pictures/park.jpg')
cv.imshow("Original", img)

gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
cv.imshow("Grayscale", gray)

# Laplacian
lap = cv.Laplacian(gray, cv.CV_64F)
lap = np.uint8(np.absolute(lap))
cv.imshow("Laplacian", lap)

# Sobel
sobelx = cv.Sobel(gray, cv.CV_64F, 1, 0)
sobely = cv.Sobel(gray, cv.CV_64F, 0, 1)
combined_sobel = cv.bitwise_or(sobelx, sobely)

cv.imshow("Sobel X", sobelx)
cv.imshow("Sobel y", sobely)
cv.imshow("Sobel Combined", combined_sobel)

# Canny
canny = cv.Canny(gray, 175, 150)
cv.imshow("Canny", canny)

cv.waitKey(0)