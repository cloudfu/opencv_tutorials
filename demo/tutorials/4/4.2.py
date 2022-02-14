# 图像的几何变换

# 缩放
import os
import numpy as np
import cv2 as cv
import matplotlib.pylab as plt

file_path = os.path.abspath(os.path.dirname(__file__))
file_path = os.path.join(file_path, "./images/img2.png")
img = cv.imread(file_path)
cv.imshow("img",img)

# 图像放大
res = cv.resize(img,None,fx=0.4, fy=0.4, interpolation = cv.INTER_CUBIC)
# #或者
# height, width = img.shape[:2]
# res = cv.resize(img,(2*width, 2*height), interpolation = cv.INTER_CUBIC)
cv.imshow("res",res)
cv.waitKey(0)



# 平移
rows,cols,color = img.shape
# [1,0,100]，第一位：代表的处理行数据，第二位代码列数据，如果行列数据为1代码当前设定激活，第三方为需要平移数据
M = np.float32([[1,0,100],[0,1,50]])

# 平移x=100 ,y=50
dst = cv.warpAffine(img,M,(cols,rows))
cv.imshow('img',dst)
cv.waitKey(0)
cv.destroyAllWindows()

# 旋转
rows,cols,color = img.shape
# 入参1：cols-1 和 rows-1 是旋转中心点
# 入参2：旋转角度
# 入参3：缩放倍数
M = cv.getRotationMatrix2D(((cols-1)/2.0,(rows-1)/2.0),90,1)
dst = cv.warpAffine(img,M,(cols,rows))
cv.imshow("dst",dst)
cv.waitKey(0)
cv.destroyAllWindows()

# 仿射变换
rows,cols,ch = img.shape
pts1 = np.float32([[50,50],[200,50],[50,200]])
pts2 = np.float32([[10,100],[200,50],[150,250]])
M = cv.getAffineTransform(pts1,pts2)
dst = cv.warpAffine(img,M,(cols,rows))
plt.subplot(121),plt.imshow(img),plt.title('Input')
plt.subplot(122),plt.imshow(dst),plt.title('Output')
plt.show()

# 透视变换
file_path = os.path.abspath(os.path.dirname(__file__))
file_path = os.path.join(file_path, "./images/perspective.jpg")
img = cv.imread(file_path)

rows,cols,ch = img.shape
pts1 = np.float32([[220,40],[1150,20],[40,545],[1270,550]])
pts2 = np.float32([[0,0],[1000,0],[0,500],[1000,500]])
M = cv.getPerspectiveTransform(pts1,pts2)
dst = cv.warpPerspective(img,M,(300,300))
plt.subplot(121),plt.imshow(img),plt.title('Input')
plt.subplot(122),plt.imshow(dst),plt.title('Output')
plt.show()