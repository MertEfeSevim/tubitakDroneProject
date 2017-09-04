import cv2
import numpy as np

kernel = np.ones((5,5),np.uint8)

liveCam = cv2.imread("deneme2.png")

frame2RGB =cv2.cvtColor(liveCam,cv2.COLOR_BGR2RGB)

frameResized = cv2.resize(liveCam, None, fx=0.2, fy=0.2, interpolation=cv2.INTER_LINEAR)

gray = cv2.cvtColor(frameResized, cv2.COLOR_BGR2GRAY)
detector = cv2.SimpleBlobDetector_create()
cannyEdge = cv2.Canny(gray, 50, 240)
dilation = cv2.dilate(cannyEdge, kernel, iterations=1)
# Detect blobs.
squares = detector.detect(dilation)
# Draw detected blobs as red circles.
# cv2.DRAW_MATCHES_FLAGS_DRAW_RICH_KEYPOINTS ensures the size of the circle corresponds to the size of blob
im_with_keypoints = cv2.drawKeypoints(gray, squares, np.array([]), (0, 0, 0),cv2.DRAW_MATCHES_FLAGS_DRAW_RICH_KEYPOINTS)


for keyPoint in squares:
    x = keyPoint.pt[0]  # i is the index of the blob you want to get the position
    y = keyPoint.pt[1]
    #print(keyPoint.size)

    #if len(squares) == 16 :#and keyPoint.size
     #   print("geldi")


    color = (frame2RGB[y,x])
    hex = (color[0] << 16) + (color[1] << 8) + (color[2])

    print("color",color)
    print("hex",hex)

cv2.imshow("Squares", im_with_keypoints)
#cv2.imshow("frame",frame)


cv2.waitKey(0)
cv2.destroyAllWindows()

"""
if np.any(rgbLive[x, y]) == [255, 255, 0]:
    print("sarı")
elif np.any(rgbLive[x, y]) == [0, 0, 255]:
    print("mavi")
elif np.any(rgbLive[x, y]) == [255, 0, 0]:
    print("yeşil")
else :
    print("bu ne amk")
"""