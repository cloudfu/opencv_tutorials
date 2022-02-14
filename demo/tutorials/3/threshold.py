import os
import cv2
import numpy as np
from matplotlib import pyplot as plt

def create_gray_image(height,width):
    gray_bg = np.zeros((height,width), np.uint8)
    for h in range(height):
        for w in range(width):
            gray_bg[h,w] = (255/width) * w
    return gray_bg

img=create_gray_image(400,600)
# 原始图像 0 - 255

# cv2.THRESH_BINARY    大于阈值的部分被置为255，小于部分被置为0
ret,thresh1=cv2.threshold(img,127,255,cv2.THRESH_BINARY)

# cv2.THRESH_BINARY_INV    大于阈值部分被置为0，小于部分被置为255    
ret,thresh2=cv2.threshold(img,127,255,cv2.THRESH_BINARY_INV)

# cv2.THRESH_TRUNC     大于阈值部分被置为threshold，小于部分保持原样  
ret,thresh3=cv2.threshold(img,127,255,cv2.THRESH_TRUNC)

# cv2.THRESH_TOZERO   小于阈值部分被置为0，大于部分保持不变
ret,thresh4=cv2.threshold(img,127,255,cv2.THRESH_TOZERO)

# cv2.THRESH_TOZERO_INV    大于阈值部分被置为0，小于部分保持不变 
ret,thresh5=cv2.threshold(img,127,255,cv2.THRESH_TOZERO_INV)
 
titles = ['Original Image','BINARY','BINARY_INV','TRUNC','TOZERO','TOZERO_INV']
images = [img, thresh1, thresh2, thresh3, thresh4, thresh5]
 
for i in range(6):
    plt.subplot(2,3,i+1), plt.imshow(images[i],'gray')
    plt.title(titles[i])
    plt.xticks([]),plt.yticks([])
plt.show()

# 关闭窗口
k = cv2.waitKey(0)
if k == ord('q'):
    cv2.DestroyWindow("gray")
    # cv2.destroyAllWindows()
