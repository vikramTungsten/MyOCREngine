import urllib

from PIL import Image
import pytesseract
from resizeimage import resizeimage
import os
import cv2
import numpy as np
#from .crop_morphology import process_image
from image_processing import crop_morphology

def get_string(img_path,output):
    # Read image with opencv
    img = cv2.imread(img_path)
    # Convert to gray
    img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

    # Apply dilation and erosion to remove some noise
    kernel = np.ones((1, 1), np.uint8)
    img = cv2.dilate(img, kernel, iterations=1)
    img = cv2.erode(img, kernel, iterations=1)

    cv2.imwrite(output, img)
    result = pytesseract.image_to_string(Image.open(output), lang='eng')
    file=open("/home/vkm/Desktop/imges/text.txt","w")
    file.write(result)
    file.close()



def get_text(path):
    print 'path',path
    out_path = path.replace('.jpg', '.crop.png')
    print 'path', out_path
    crop_morphology.process_image(path,out_path)
    out_path1 = out_path.replace('.crop.png', '.removed_noise.png')
    get_string(out_path,out_path1)


get_text('/home/vkm/Desktop/imges/Public-Notice-in-Newspaper.jpg')