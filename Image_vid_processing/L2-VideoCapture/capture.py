from cv2 import cv2
import time

video = cv2.VideoCapture(0)
while True:

    check, frame = video.read()
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    cv2.imshow("gray Frame", gray)
    key = cv2.waitKey(1000)
    if key == ord('q'):
        break
    else:
        pass

video.release()
cv2.destroyAllWindows()
