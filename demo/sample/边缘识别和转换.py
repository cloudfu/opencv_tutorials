#! /usr/bin/env python
# -*- coding: utf-8 -*-

import os
import numpy as np
import cv2
import imutils


# 使用opencv的cv2.getPerspctiveTransform函数将图像进行透视变化。
# 最关键的在于确定矩形的顶点，逆时针或顺时针排列都可以，同时确定目标参考点也同样重要。

"""
x小y小rect[0]  x大y小rect[1]
	-------------
	|           |
	|           |
	-------------
x小y大rect[3]  x大y大rect[2]
"""


def order_points(pts):
    # 初始化矩形4个顶点的坐标
    rect = np.zeros((4, 2), dtype='float32')
    # 坐标点求和 x+y
    s = pts.sum(axis=1)
    # np.argmin(s) 返回最小值在s中的序号
    rect[0] = pts[np.argmin(s)]
    rect[2] = pts[np.argmax(s)]
    # diff就是后一个元素减去前一个元素  y-x
    diff = np.diff(pts, axis=1)
    rect[1] = pts[np.argmin(diff)]
    rect[3] = pts[np.argmax(diff)]
    # 返回矩形有序的4个坐标点
    return rect


def perTran(image, pts):
    rect = order_points(pts)
    tl, tr, br, bl = rect
    # 计算宽度
    widthA = np.sqrt(((br[0] - bl[0]) ** 2) + ((br[1] - bl[1]) ** 2))
    widthB = np.sqrt(((tr[0] - tl[0]) ** 2) + ((tr[1] - tl[1]) ** 2))
    maxWidth = max(int(widthA), int(widthB))
    # 计算高度
    heightA = np.sqrt(((tr[0] - br[0]) ** 2) + ((tr[1] - br[1]) ** 2))
    heightB = np.sqrt(((tl[0] - bl[0]) ** 2) + ((tl[1] - bl[1]) ** 2))
    maxHeight = max(int(heightA), int(heightB))
    # 定义变换后新图像的尺寸
    dst = np.array([[0, 0], [maxWidth - 1, 0], [maxWidth - 1, maxHeight - 1],
                    [0, maxHeight - 1]], dtype='float32')
    # 变换矩阵
    M = cv2.getPerspectiveTransform(rect, dst)
    # 透视变换
    warped = cv2.warpPerspective(image, M, (maxWidth, maxHeight))
    return warped


def main():

    image = cv2.imread("./opencv_sample/images/hello.png")
    output = image.copy()

    # 转换成灰度图像
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

    # 双边滤波器能够做到平滑去噪的同时还能够很好的保存边缘

    # bilateralFilter 入参说明
    # src：输入图像
    # d：过滤时周围每个像素领域的直径
    # sigmaColor：在color space中过滤sigma。参数越大，临近像素将会在越远的地方mix。
    # sigmaSpace：在coordinate space中过滤sigma。参数越大，那些颜色足够相近的的颜色的影响越大。
    gray = cv2.bilateralFilter(gray, 11, 17, 17)
    
    # 检测边缘
    edged = cv2.Canny(gray, 30, 200)
    # cv2.imshow('Canny', edged)
    # 查找轮廓
    cnts = cv2.findContours(edged.copy(), cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
    cnts = imutils.grab_contours(cnts)
    # 获取前3个最大的轮廓
    cnts = sorted(cnts, key=cv2.contourArea, reverse=True)[:3]

    screenCnt = None
    for c in cnts:
        # 轮廓周长
        peri = cv2.arcLength(c, True)
        print('arcLength : {:.3f}'.format(peri))
        # approxPolyDP主要功能是把一个连续光滑曲线折线化，对图像轮廓点进行多边形拟合。
        # 近似轮廓的多边形曲线， 近似精度为轮廓周长的1.5%
        approx = cv2.approxPolyDP(c, 0.015 * peri, True)
        # 矩形边框具有4个点， 将其他的剔除
        if len(approx) == 4:
            screenCnt = approx
            break
    # 绘制轮廓矩形边框
    cv2.drawContours(image, [screenCnt], -1, (0, 255, 0), 3)
    # 调整为x,y 坐标点矩阵
    pts = screenCnt.reshape(4, 2)
    # print('screenCnt.reshape:\n{}'.format(pts))
    # 透视变换
    warped = perTran(output, pts)

    cv2.imshow('image', image)
    cv2.imshow('output', output)
    cv2.imshow('warped', warped)

    cv2.waitKey(0)
    cv2.destroyAllWindows()


if __name__ == "__main__":
    print(os.getcwd())
    main()
