import cv2
import numpy as np

liveCam = cv2.VideoCapture(0)

while True:

    _,frame = liveCam.read()


    detector = cv2.SimpleBlobDetector_create()

    #cannyEdge = cv2.Canny(frame,50,240)

    # Detect blobs.
    squares = detector.detect(frame)

    # Draw detected blobs as red circles.
    # cv2.DRAW_MATCHES_FLAGS_DRAW_RICH_KEYPOINTS ensures the size of the circle corresponds to the size of blob
    im_with_keypoints = cv2.drawKeypoints(frame, squares, np.array([]), (0, 0, 0),cv2.DRAW_MATCHES_FLAGS_DRAW_RICH_KEYPOINTS)


    for keyPoint in squares:
        x = keyPoint.pt[0]  # i is the index of the blob you want to get the position
        y = keyPoint.pt[1]

        print("(",x,",",y,")")
    #print(len(squares),"tane kare var.")

    cv2.imshow("Squares", im_with_keypoints)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

liveCam.release()
cv2.destroyAllWindows()