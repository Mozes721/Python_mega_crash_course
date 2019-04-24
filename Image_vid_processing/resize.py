import cv2
import glob
import os
path="Image_vid_processing/img_folder"

files = os.listdir(path)

for name in files:
    im = cv2.imread("Image_vid_processing/img_folder/"+ name,0)
    cv2.imwrite(path+"/"+name[:-4]+"2.jpg",cv2.resize(im(100,100)))
