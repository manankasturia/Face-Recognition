import cv2 as cv

img = cv.imread('pictures/group 1.jpg')
cv.imshow("Group of People", img)

# mainly two built-in ways to detect faces in opencv: haar cascades and local binary pattern(more advanced)
gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
cv.imshow("Gray Group", gray)

haar_cascade = cv.CascadeClassifier('haarcascade_face.xml')

faces_rect = haar_cascade.detectMultiScale(gray, scaleFactor=1.1, minNeighbors=1)
print("Number of faces found = ", len(faces_rect))

for (x, y, w, h) in faces_rect:
    cv.rectangle(img, (x,y), (x+w, y+h), (0,255,0), thickness=2)

cv.imshow("Detected Faces", img)

cv.waitKey(0)