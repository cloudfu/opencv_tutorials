# OpenCV中有超过150种颜色空间转换方法。但是我们将研究只有两个最广泛使用的,BGR↔灰色和BGR↔HSV。
# 对于BGR→灰度转换，我们使用标志cv.COLOR_BGR2GRAY。类似地
# 对于BGR→HSV，我们使用标志cv.COLOR_BGR2HSV。要获取其他标记，只需在Python终端中运行以下命令:

# H参数表示色彩信息，即所处的光谱颜色的位置。该参数用一角度量来表示，红、绿、蓝分别相隔120度。互补色分别相差180度。
# 纯度S为一比例值，范围从0到1，它表示成所选颜色的纯度和该颜色最大的纯度之间的比率。S=0时，只有灰度。
# V表示色彩的明亮程度，范围从0到1。有一点要注意：它和光强度之间并没有直接的联系。

import os
import cv2 as cv
import numpy as np
cap = cv.VideoCapture(0)

while(1):
    # 读取帧
    _, frame = cap.read()
    # 转换颜色空间 BGR 到 HSV
    hsv = cv.cvtColor(frame, cv.COLOR_BGR2HSV)
    # 定义HSV中蓝色的范围
    # RGB 取色
    lower_blue = np.array([0, 60, 60])
    upper_blue = np.array([6, 255, 255])
    # 设置HSV的阈值使得只取蓝色
    # 第二个参数：lower_red指的是图像中低于这个lower_red的值，图像值变为0
    # 第三个参数：upper_red指的是图像中高于这个upper_red的值，图像值变为0
    # 在区间值中间的显示白色255
    mask = cv.inRange(hsv, lower_blue, upper_blue)
    # 将掩膜和图像逐像素相加
    res = cv.bitwise_and(frame,frame, mask= mask)
    cv.imshow('frame',frame)

    # 显示白色
    cv.imshow('mask',mask)

    # 显示蓝色
    cv.imshow('res',res)
    k = cv.waitKey(5) & 0xFF
    if k == 27:
        break

cv.destroyAllWindows()


# 查找HSV 浮动值
green = np.uint8([[[0,255,0 ]]])
hsv_green = cv.cvtColor(green,cv.COLOR_BGR2HSV)
print( hsv_green ) # [[[ 60 255 255]]]
# 现在把[H- 10,100,100]和[H+ 10,255, 255]分别作为下界和上界。


# file_path = os.path.abspath(os.path.dirname(__file__))
# file_path = os.path.join(file_path, "./images/img2.png")
# frame = cv.imread(file_path)

# # 转换颜色空间 BGR 到 HSV
# hsv = cv.cvtColor(frame, cv.COLOR_BGR2HSV)
# # 定义HSV中蓝色的范围
# lower_blue = np.array([110,50,50])
# upper_blue = np.array([130,255,255])
# # 设置HSV的阈值使得只取蓝色
# mask = cv.inRange(hsv, lower_blue, upper_blue)
# # 将掩膜和图像逐像素相加
# res = cv.bitwise_and(frame,frame, mask= mask)
# cv.imshow('frame',frame)
# cv.imshow('mask',mask)
# cv.imshow('res',res)
# k = cv.waitKey(0)
