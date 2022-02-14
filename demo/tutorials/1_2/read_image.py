import os
import cv2
import numpy as np
import matplotlib.pyplot as plt

# 开始计时
start = cv2.getTickCount()


# 使用相对路径加载图片路径
my_path = os.path.abspath(os.path.dirname(__file__))
image_path = os.path.join(my_path, "../../01-Introduction-and-Installation/lena.jpg")

# 读入一张图片并调整对比度和亮度
# cv2.IMREAD_COLOR 彩色图片读取
# cv2.IMREAD_GRAYSCALE 灰度方式读取
# cv2.IMREAD_UNCHANGED 包括透明读取
img1 = cv2.imread(image_path,cv2.IMREAD_GRAYSCALE)
img2 = np.uint8(np.clip((img1 + 20), 0, 255))

img_merger = np.hstack((img1, img2))

# cv2.WINDOW_NORMAL 可调整大小，图像会随着大小进行伸缩
# cv2.WINDOW_AUTOSIZE 默认大小，自动调整图像大小，不能进行缩放
cv2.namedWindow('Hello', cv2.WINDOW_AUTOSIZE)
cv2.imshow("Hello",img_merger)

# 停止计时
end = cv2.getTickCount()

# 单位：s
print((end - start) / cv2.getTickFrequency())

# 通过 pyplot 显示图片
# plt.imshow(img1, cmap = 'gray', interpolation = 'bicubic')
# plt.xticks([]), plt.yticks([])  # 隐藏 x 轴和 y 轴上的刻度值
# plt.show()

# 关闭窗口
k = cv2.waitKey(0)
if k == ord('q'):
    cv2.DestroyWindow("Hello")
    # cv2.destroyAllWindows()

