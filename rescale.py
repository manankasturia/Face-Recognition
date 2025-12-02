import cv2 as cv

# scale is the value by which the frame should be rescaled
# it is better to set it to less than 1(smaller than current size) because it may be showing frame now at its maximum capability
def rescaleFrame(frame, scale = 0.75):
    # this function can be used for images, video and live video through webcam
    width = int(frame.shape[1] * scale) # shape[1] is the width of current frame
    height = int(frame.shape[0] * scale) # shape[0] is the height of current frame
    # typecasted them to int as height and width of an image are always integer
    # dimensions of an image is of form width × height(shape[1], shape[0])

    dimensions = (width, height)

    return cv.resize(frame, dimensions, interpolation=cv.INTER_AREA)

def changeRes(width, height):
    # this function can be used just for live video through webcam
    capture.set(3, width) # 3 references to width
    capture.set(4, height) # 4 references to height

# image rescaling
img = cv.imread('pictures/dog pups.jpeg')
img_resized = rescaleFrame(img, 0.1)

cv.imshow('Dog Photo Original', img)
cv.imshow('Dog Photo Resized', img_resized) # dog photo reduced to 10%

cv.waitKey(0)

# video rescaling
capture = cv.VideoCapture('videos/dog.mp4')

while True:
    isTrue, frame = capture.read()
    frame_resized = rescaleFrame(frame)
    cv.imshow('Dog Video Original', frame)
    cv.imshow('Dog Video resized', frame_resized)

    if cv.waitKey(20) & 0xFF==ord('d'):
        break

capture.release()
cv.destroyAllWindows