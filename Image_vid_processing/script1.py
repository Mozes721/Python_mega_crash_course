import cv2


img=cv2.imread('C:/Users/Richa/OneDrive/Desktop/Python_mega_course-master/Image_vid_processing/galaxy.jpg')

print(img)
print(img.shape)
print(img.ndim)

resized_img= cv2.resize(img,(1000,500))
cv2.imshow("Galaxy", resized_img)
cv2.waitKey(0)
cv2.destroyAllWindows()
