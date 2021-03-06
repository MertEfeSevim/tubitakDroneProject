def coordinator():
    kernel = np.ones((15,15),np.uint8)

    liveCam = cv2.VideoCapture(0)

    if not liveCam.isOpened():
        raise IOError("Cannot access camera.")

    while True:

        _,frame = liveCam.read()

        frameRGB = cv2.cvtColor(frame,cv2.COLOR_BGR2RGB)

        #frameResized = cv2.resize(frame, None, fx=0.5, fy=0.5, interpolation=cv2.INTER_LINEAR)

        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

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

            if len(squares) == 16 :#and keyPoint.size
                #print("geldi")
                print(str(frameRGB[x, y]))



        cv2.imshow("Squares", im_with_keypoints)
        #cv2.imshow("frame",frame)

        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    liveCam.release()
    cv2.destroyAllWindows()

if __name__ == '__main__':
    import cv2
    import numpy as np

    coordinator()