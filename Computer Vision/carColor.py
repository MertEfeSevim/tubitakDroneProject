import cv2
import numpy as np

kernel = np.ones((5,5),np.uint8)

liveCam = cv2.imread("araba.jpg")

ret,thresh2 = cv2.threshold(liveCam,127,255,cv2.THRESH_BINARY)
dilate = cv2.dilate(thresh2,kernel)

cv2.imshow('result', dilate)


cv2.waitKey(0)
cv2.destroyAllWindows()
