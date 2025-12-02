import cv2 as cv
import numpy as np
import matplotlib.pyplot as plt

img = cv.imread('pictures/cats 2.jpg')
cv.imshow("Original", img)

gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
cv.imshow("Grayscale", gray)

blank = np.zeros(img.shape[:2], dtype='uint8')
circle = cv.circle(blank, (img.shape[1]//2,img.shape[0]//2), 100, 255, -1)

mask = cv.bitwise_and(gray, gray, mask=circle)
cv.imshow("Masked Grayscale", mask)

# Grayscale Histogram
gray_hist = cv.calcHist([gray], [0], None, [256], [0,256])

plt.figure()
plt.title('Grayscale Histogram')
plt.xlabel('Bins')
plt.ylabel('# of pixels')
plt.plot(gray_hist)
plt.xlim([0,256])
plt.show()

# Masked Grayscale Histogram
maskgray_hist = cv.calcHist([gray], [0], mask, [256], [0,256])

plt.figure()
plt.title('Masked Grayscale Histogram')
plt.xlabel('Bins')
plt.ylabel('# of pixels')
plt.plot(maskgray_hist)
plt.xlim([0,256])
plt.show()

# Color Histogram
plt.figure()
plt.title('Color Histogram')
plt.xlabel('Bins')
plt.ylabel('# of pixels')
colors = ('b', 'g', 'r')
for i, col in enumerate(colors):
    hist = cv.calcHist([img], [i], None, [256], [0,256])
    plt.plot(hist, color=col)
    plt.xlim([0,256])
plt.show()

cv.waitKey(0)