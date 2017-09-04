import cv2
import numpy as np

liveCam = cv2.VideoCapture(0)

while 1:
    _, frame = liveCam.read()
    gray = cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)

    gray = np.float32(gray)
    dst = cv2.cornerHarris(gray,2,3,0.04)


    # Threshold for an optimal value, it may vary depending on the image.
    frame[dst>0.01*dst.max()]=[0,0,255]

    cv2.imshow('dst',frame)

    if cv2.waitKey(0) & 0xff == 27:
        break

liveCam.release()
cv2.destroyAllWindows()