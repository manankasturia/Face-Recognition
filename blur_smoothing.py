import cv2 as cv

img= cv.imread('pictures/cats.jpg')
cv.imshow("Original", img)

# Averaging - averaging all 8 pixels surrounding a pixel and setting average value to middle pixel (for (3,3) kernel size)
average = cv.blur(img, (3,3))
cv.imshow("Average Blur", average)

# Gaussian - this method gives each pixel a weight then it does the same averaging as average blur (more natural blur)
gauss = cv.GaussianBlur(img, (3,3), 0)
cv.imshow("Gaussian Blur", gauss)

# Median - instead of average this method uses median of all the surrounding pixels and display it in middle (good noise reduction)
median = cv.medianBlur(img, 3)
cv.imshow("Median Blur", median)

# Bilateral - it blurs the image but retains the edges (rest all blur method blurs the whole image, this method leaves edges)
bilateral = cv.bilateralFilter(img, 5, 15, 16) # 5 is the diameter
# 16 is sigma space means how far way pixel should influence pixel blur is being applied to
cv.imshow("Bilateral", bilateral)


cv.waitKey(0)