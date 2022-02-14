import os
import  cv2
import numpy as np

# img1 = cv.imread('ml.png')
# img2 = cv.imread('opencv-logo.png')
# dst = cv.addWeighted(img1,0.7,img2,0.3,0)
# cv.imshow('dst',dst)
# cv.waitKey(0)
# cv.destroyAllWindows()


# -----------------
# 按位运算
# -----------------
# 加载两张图片
file_path = os.path.abspath(os.path.dirname(__file__))
img_bg_path = os.path.join(file_path, "./images/img2.png")
img_logo_path = os.path.join(file_path, "./images/logo.jpg")

img_bg = cv2.imread(img_bg_path)
img_logo = cv2.imread(img_logo_path)

# 通过获取logo大小，在back_image上获取ROI
rows,cols,channels = img_logo.shape
roi = img_bg[0:rows, 0:cols ]

# img_logo：灰度处理
img2gray = cv2.cvtColor(img_logo,cv2.COLOR_BGR2GRAY)
# img_logo：二值化 白化处理
ret, mask = cv2.threshold(img2gray, 10, 255, cv2.THRESH_BINARY)
# img_logo：反转 黑化处理
mask_inv = cv2.bitwise_not(mask)

# OpenCV 按位bitwise运算、掩膜mask运算详解 表格+图解 Python代码实例详解 基础实用款
# https://blog.csdn.net/yl_best/article/details/87877110

# 现在将ROI中logo的区域涂黑
img1_bg = cv2.bitwise_and(roi,roi,mask = mask_inv)
# 仅从logo图像中提取logo区域
img2_fg = cv2.bitwise_and(img_logo,img_logo,mask = mask)
# 将logo放入ROI并修改主图像
dst = cv2.add(img1_bg,img2_fg)
cv2.imshow('img1_bg',dst)
img_bg[0:rows, 0:cols ] = dst
# cv2.imshow('res',img_bg)
cv2.waitKey(0)
cv2.destroyAllWindows()