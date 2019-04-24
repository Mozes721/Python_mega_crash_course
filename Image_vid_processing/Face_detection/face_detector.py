import cv2

face_cascade = cv2.CascadeClassifier(
    "C:/Users/Richa/OneDrive/Desktop/Python_mega_course-master/Image_vid_processing/Face_detection/haarcascade_frontalface_default.xml")

img = cv2.imread(
    "C:/Users/Richa/OneDrive/Desktop/Python_mega_course-master/Image_vid_processing/Face_detection/photo.jpg", 0)
gray_img = cv2.cvtColor(img, cv2.COLOR_BAYER_BG2GRAY)

faces = face_cascade.detectMultiScale(gray_img, scaleFactor=1.5,
                                      minNeighbors=5)

for x, y, w, h in faces:
    img = cv2.rectangle(img, (x, y), (x+w, y+h), (0, 255, 0), 3)


print(faces)

cv2.imshow("Gray", img)
cv2.waitKey(0)
cv2.destroyAllWindows()
