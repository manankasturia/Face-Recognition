import cv2 as cv

capture = cv.VideoCapture('videos/dog.mp4') # 540 × 960 video size

while True:
    isTrue, frame = capture.read()
    cv.imshow('Dog Video', frame)

    if cv.waitKey(20) & 0xFF==ord('d'): # will break out of loop if we press d
        break
# opencv breaks out of loop because it couldn't find more frames to show after the last frame and display -215 error

capture.release()
cv.destroyAllWindows