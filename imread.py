import cv2 as cv
import numpy as np


img =cv.imread('e:/cat.jpg')
print(img.shape)
new =cv.cvtColor(img,cv.COLOR_BGR2GRAY)
print(new.shape)
print(img.size)
print(img.dtype)
