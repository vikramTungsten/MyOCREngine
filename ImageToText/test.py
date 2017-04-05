import urllib

from PIL import Image
import pytesseract
from resizeimage import resizeimage
import os
import cv2
import numpy as np

src_path = "/home/vkm/PycharmProjects/ImageToText/Test1/"


def get_string(img_path):
    result = pytesseract.image_to_string(Image.open('/home/vkm/PycharmProjects/ImageToText/Test/2.png'), lang='eng')
    # os.remove(temp)
    return result


print '--- Start recognize text from image ---'
print get_string("/home/vkm/PycharmProjects/ImageToText/Images/2.png")

print "------ Done -------"
