import cv2 as cv
import numpy as np

img = cv.imread('pictures/cats.jpg')
cv.imshow("Original", img)

blank = np.zeros(img.shape[:2], dtype='uint8') # mask should be of same dimensions as original image

mask = cv.circle(blank.copy(), (img.shape[1]//2,img.shape[0]//2), 100, 255, -1)
cv.imshow("Mask", mask)

masked = cv.bitwise_and(img, img, mask=mask)
cv.imshow("Masked Image", masked)

# wierd mask
rectangle = cv.rectangle(blank.copy(), (img.shape[1]//2-50,img.shape[0]//2-50), (img.shape[1]//2+150,img.shape[0]//2+150), 255, -1)
cv.imshow("Rectangle mask", rectangle)

wierdMask = cv.bitwise_and(mask, rectangle)
cv.imshow("Wierd Mask", wierdMask)

wierdMasked = cv.bitwise_and(img, img, mask=wierdMask)
cv.imshow("wierd Masked Image", wierdMasked)

cv.waitKey(0)