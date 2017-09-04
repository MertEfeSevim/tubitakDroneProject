def coordinator():
    kernel = np.ones((15,15),np.uint8)

    liveCam = cv2.VideoCapture(0)

    if not liveCam.isOpened():
        raise IOError("Cannot access camera.")

    while True:

        ret,frame = liveCam.read()

        gray = cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
        ret, thresh = cv2.threshold(gray, 0, 255, 0)
        contours = cv2.findContours(thresh, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)[-2]

        cv2.drawContours(frame, contours, -1, (255, 0, 255), 2)

        cv2.imshow("contour",frame)
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    liveCam.release()
    cv2.destroyAllWindows()

if __name__ == '__main__':
    import cv2
    import numpy as np

    coordinator()