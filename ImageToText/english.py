import urllib

from PIL import Image
import pytesseract
from resizeimage import resizeimage
import os
import cv2
import numpy as np

src_path = "/home/vkm/PycharmProjects/ImageToText/Test1/"


def get_string(img_path):
    # Read image with opencv
    img = cv2.imread(img_path)
    # Convert to gray
    img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

    # Apply dilation and erosion to remove some noise
    kernel = np.ones((1, 1), np.uint8)
    img = cv2.dilate(img, kernel, iterations=1)
    img = cv2.erode(img, kernel, iterations=1)

    cv2.imwrite(src_path + "removed_noise.png", img)

    # Apply threshold to get image with only black and white
    img = cv2.adaptiveThreshold(img, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY, 11, 2)

    # Write the image after apply opencv to do some ...
    cv2.imwrite(src_path + "thres.png", img)

    # Recognize text with tesseract for python
    print '============>', src_path + "thres.png"

    result = pytesseract.image_to_string(Image.open(src_path + "removed_noise.png"), lang='eng')
    file=open("/home/vkm/Desktop/imges/text.txt","w")
    file.write(result)
    file.close()
    print result

    # os.remove(temp)
    return result


print '--- Start recognize text from image ---'
print get_string("/home/vkm/Desktop/imges/Public-Notice-in-Newspaper.crop.png")

print "------ Done -------"
