def coordinator():
    kernel = np.ones((5,5),np.uint8)

    liveCam = cv2.VideoCapture(0)

    while True:

        _,frame = liveCam.read()
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

            #col = str(frame[x,y])
            #print(col)

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

#print(frame[x, y])
#hex = (color[0] << 16) + (color[1] << 8) + (color[2])
#print("(",x,",",y,")")
#print(len(squares),"tane kare var.")