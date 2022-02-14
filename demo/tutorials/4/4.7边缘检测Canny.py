import os
import numpy as np
import cv2 as cv
from matplotlib import pyplot as plt

# OpenCV中的Canny边缘检测

# 透视变换
img = cv.imread("./OpenCV_Demo/4/images/perspective.jpg")

edges = cv.Canny(img,100,200)
plt.subplot(121),plt.imshow(img,cmap = 'gray')
plt.title('Original Image'), plt.xticks([]), plt.yticks([])
plt.subplot(122),plt.imshow(edges,cmap = 'Blues')
plt.title('Edge Image'), plt.xticks([]), plt.yticks([])
plt.show()

# key = cv.waitKey(0)