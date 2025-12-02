import cv2 as cv
import numpy as np

blank = np.zeros((400,400), dtype='uint8')

rectangle = cv.rectangle(blank.copy(), (30,30), (370,370), 255, -1)
circle = cv.circle(blank.copy(), (200,200), 200, 255, -1)

cv.imshow("Rectangle", rectangle)
cv.imshow("Circle", circle)

# in bitwise operations 0 means black and 1 means white

# bitwise AND - returns intersection of two images
bitwise_and = cv.bitwise_and(rectangle, circle)
cv.imshow("Bitwise AND", bitwise_and)

# biwise OR - returns union of two images
bitwise_or = cv.bitwise_or(rectangle, circle)
cv.imshow("Bitwise OR", bitwise_or)

# bitwise XOR - returns 1 for only the regions which are not intersecting
bitwise_xor = cv.bitwise_xor(rectangle, circle)
cv.imshow("Bitwise XOR", bitwise_xor)

# bitwise NOT - returns black where there is white and white where there is black
bitwise_not = cv.bitwise_not(rectangle)
cv.imshow("Bitwise NOT", bitwise_not)

cv.waitKey(0)