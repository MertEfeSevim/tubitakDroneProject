import cv2
import numpy as np

filename = 'deneme.png'

img = cv2.imread(filename)
# Set up the detector with default parameters.
detector = cv2.SimpleBlobDetector_create()

# Detect blobs.
keypoints = detector.detect(img)


# Draw detected blobs as red circles.
# cv2.DRAW_MATCHES_FLAGS_DRAW_RICH_KEYPOINTS ensures the size of the circle corresponds to the size of blob
im_with_keypoints = cv2.drawKeypoints(img, keypoints, np.array([]), (0, 0, 0),cv2.DRAW_MATCHES_FLAGS_DRAW_RICH_KEYPOINTS)


for keyPoint in keypoints:
    x = keyPoint.pt[0]  # i is the index of the blob you want to get the position
    y = keyPoint.pt[1]
    print("x ",x)
    print("y ",y)
    print(" ")

cv2.imshow("Keypoints", im_with_keypoints)

if cv2.waitKey(1) & 0xFF == ord('q'):
    cv2.destroyAllWindows()

