import cv2 as cv
import numpy as np

img = cv.imread('pictures/cat.jpg')
cv.imshow('Original', img)

# Translate - shifts image by specified pixels on the axis
def translate(img, x, y):
    transMat = np.float32([[1,0,x],[0,1,y]])
    dimensions = (img.shape[1], img.shape[0])
    return cv.warpAffine(img, transMat, dimensions)

# -x --> Left, x --> Right
# -y --> Up, y --> Down

translated = translate(img, 100, 100) # shifts image right by 100 pixels and down by 100 pixels
cv.imshow("Translated", translated)

# Rotate - rotates image around any arbitary point in the image
def rotate(img, angle, rotPoint = None):
    (height, width) = img.shape[:2]

    if rotPoint is None:
        rotPoint = (width//2, height//2)

    rotMat = cv.getRotationMatrix2D(rotPoint, angle, 1.0)
    dimensions = (width, height)

    return cv.warpAffine(img, rotMat, dimensions)

# angle --> anticlockwise, -angle --> clockwise
rotated = rotate(img, 45)
cv.imshow("Rotated", rotated)

# Resizing
resized = cv.resize(img, (500, 500), interpolation=cv.INTER_AREA)
cv.imshow("Resized", resized)

# Flipping
flip = cv.flip(img, 0) # 0: flip vertically, 1: flip horizontally, -1: flip both vertically and horizontally
cv.imshow("Flipped", flip)

# Cropping
cropped = img[:500, 100:600]
cv.imshow("Cropped", cropped)

cv.waitKey(0)