import cv2 as cv

img = cv.imread('pictures/cat.jpg')
cv.imshow("Original", img)

# Converting to grayscale
gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
cv.imshow("Grayscale", gray)

# Converting Blur
blur = cv.GaussianBlur(img, (5,5), cv.BORDER_DEFAULT)
#                           Kernel size tuple(changes blur intensity)
cv.imshow("Blur", blur)

# Edge cascade
canny = cv.Canny(img, 125, 175)
cv.imshow("Canny Edges", canny)

# Dilating the images
dilated = cv.dilate(canny, (3,3), iterations=2)
cv.imshow("Dilated", dilated)

# Eroding the image(getting canny back from dilated)
eroded = cv.erode(dilated, (3,3), iterations=2)
cv.imshow("Eroded", eroded)

# Resizing the image
resized = cv.resize(img, (500,500), interpolation=cv.INTER_AREA) # we use INTER_AREA when decreasing size of image
# if we want to increase size of image the we either use INTER_LINEAR or INTER_CUBIC(slower but better quality)
cv.imshow("Resized", resized)

# Cropping the image
cropped = img[200:500, 100:600] # image is array of pixels and each pixel can be written in (B,G,R), so we can split that array
cv.imshow("Cropped", cropped)

cv.waitKey(0)