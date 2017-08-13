import cv2
import numpy as np,time

liveCam = cv2.imread("deneme2.png",cv2.IMREAD_GRAYSCALE)

detector = cv2.SimpleBlobDetector_create()
th = cv2.adaptiveThreshold(liveCam, 255, cv2.ADAPTIVE_THRESH_MEAN_C, cv2.THRESH_BINARY, 115, 1)

# Detect blobs.
squares = detector.detect(th)

# Draw detected blobs as red circles.
# cv2.DRAW_MATCHES_FLAGS_DRAW_RICH_KEYPOINTS ensures the size of the circle corresponds to the size of blob
im_with_keypoints = cv2.drawKeypoints(th, squares, np.array([]), (0, 0, 0),cv2.DRAW_MATCHES_FLAGS_DRAW_RICH_KEYPOINTS)


for keyPoint in squares:
    x = keyPoint.pt[0]  # i is the index of the blob you want to get the position
    y = keyPoint.pt[1]

    #print("(",x,",",y,")")
print(len(squares),"tane kare var.")

cv2.imshow("Squares", im_with_keypoints)
cv2.waitKey(0)
cv2.destroyAllWindows()

