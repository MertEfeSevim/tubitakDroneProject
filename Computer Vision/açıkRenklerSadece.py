import cv2
import numpy as np,time

img = cv2.imread("deneme2.png",cv2.IMREAD_GRAYSCALE)
retval, threshold = cv2.threshold(img, 200, 255, cv2.THRESH_BINARY_INV)

params = cv2.SimpleBlobDetector_Params()

# Change thresholds
params.minThreshold = 10;
params.maxThreshold = 255;

blur = cv2.GaussianBlur(img,(5,5),0)

params.filterByCircularity = True
params.minCircularity = 0.2

params.filterByArea = True;
params.minArea = 1000;

detector = cv2.SimpleBlobDetector_create(params)

# Set up the detector with default parameters.
#detector = cv2.SimpleBlobDetector()

# Detect blobs.
keypoints = detector.detect(threshold)

# Draw detected blobs as red circles.
# cv2.DRAW_MATCHES_FLAGS_DRAW_RICH_KEYPOINTS ensures the size of the circle corresponds to the size of blob
im_with_keypoints = cv2.drawKeypoints(img, keypoints, np.array([]), (0,0,255), cv2.DRAW_MATCHES_FLAGS_DRAW_RICH_KEYPOINTS)


for keyPoint in keypoints:
    x = keyPoint.pt[0]  # i is the index of the blob you want to get the position
    y = keyPoint.pt[1]

    #print("(",x,",",y,")")
print(len(keypoints),"tane kare var.")

# Show keypoints
cv2.imshow("Keypoints", im_with_keypoints)
cv2.waitKey(0)
