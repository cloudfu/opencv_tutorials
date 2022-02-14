import os
import cv2


# 使用相对路径加载图片路径
my_path = os.path.abspath(os.path.dirname(__file__))
image_path = os.path.join(my_path, "../01-Introduction-and-Installation/lena.jpg")

img = cv2.imread(image_path)

# 1.获取像素的值
px = img[100, 90]
print(px)  # [103 98 197]

# 只获取蓝色blue通道的值
px_blue = img[100, 90, 0]
print(px_blue)  # 103


# 2.修改像素的值
img[100, 90] = [255, 255, 255]
print(img[100, 90])  # [255 255 255]


# 3.图片形状
print(img.shape)  # (263, 247, 3)
# 形状中包括行数、列数和通道数
height, width, channels = img.shape
# img是灰度图的话：height, width = img.shape

# 总像素数
print(img.size)  # 263*247*3=194883
# 数据类型
print(img.dtype)  # uint8


# 4.ROI截取
face = img[100:200, 115:188]
cv2.imshow('face', face)
cv2.waitKey(0)


# 5.通道分割与合并
b, g, r = cv2.split(img)
img = cv2.merge((b, g, r))
# 更推荐的获取某一通道方式
b = img[:, :, 0]
cv2.imshow('b', b)
cv2.waitKey(0)
