import cv2
import numpy as np;

# Read image
im = cv2.imread("deneme2.png", cv2.IMREAD_GRAYSCALE)

# Set up the detector with default parameters.
im=cv2.bitwise_not(im)

params = cv2.SimpleBlobDetector_Params()
detector = cv2.SimpleBlobDetector_create(params)


# Detect blobs.
keypoints = detector.detect(im)
im=cv2.bitwise_not(im)
# Draw detected blobs as red circles.
# cv2.DRAW_MATCHES_FLAGS_DRAW_RICH_KEYPOINTS ensures the size of the circle corresponds to the size of blob
im_with_keypoints = cv2.drawKeypoints(im, keypoints, np.array([]), (0,0,0), cv2.DRAW_MATCHES_FLAGS_DRAW_RICH_KEYPOINTS)



for keyPoint in keypoints:
    x = keyPoint.pt[0]  # i is the index of the blob you want to get the position
    y = keyPoint.pt[1]

    #print("(",x,",",y,")")
print(len(keypoints),"tane kare var.")

# Show keypoints
cv2.imshow("Keypoints", im_with_keypoints)
cv2.waitKey(0)