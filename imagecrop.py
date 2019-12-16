import cv2
import numpy as np
import os
import sys

argc = len(sys.argv)
border = 2
basePath = "output_networks/pothole/"
if argc > 1:
    srcName = sys.argv[1]
else:
    srcName = "pothole_s5_i96000_fullavg1.jpg"

src = cv2.imread(basePath+srcName)
srcHeight, srcWidth = src.shape[:2]
cropWidth, cropHeight = 128, 128
if not os.path.exists(basePath+"crop"):
    os.makedirs(basePath+"crop")

idx = 1
for y in range(border, srcHeight, cropHeight+border):
    for x in range(border, srcWidth, cropWidth+border):
        crop = src[y:y+cropHeight, x:x+cropWidth]
        savePath = basePath+"crop/"+srcName.split(".jpg")[0]+"_"+str(idx)+".jpg"
        cv2.imwrite(savePath, crop)
        idx+=1
        
