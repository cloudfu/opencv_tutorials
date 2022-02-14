from asyncio.windows_events import NULL
import os
import numpy as np
import cv2 as cv
from matplotlib import pyplot as plt

print(os.getcwd())

img = cv.imread("./images/filter.jpg")
kernel = np.ones((3,3),np.float32)/9
blur = cv.blur(img,(5,5))

if img is not None:
    dst = cv.filter2D(img,-1,kernel)
    plt.subplot(131),plt.imshow(img),plt.title('Original')
    plt.xticks([]), plt.yticks([])
    plt.subplot(132),plt.imshow(dst),plt.title('Averaging')
    plt.xticks([]), plt.yticks([])
    plt.subplot(133),plt.imshow(blur),plt.title('Blurred')
    plt.xticks([]), plt.yticks([])
    plt.show()
else:
    print("image is none")
