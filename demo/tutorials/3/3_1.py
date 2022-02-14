import numpy as np
import cv2
import os
from matplotlib import pyplot as plt


file_path = os.path.abspath(os.path.dirname(__file__))
image_path = os.path.join(file_path, "../../01-Introduction-and-Installation/lena.jpg")

# 访问每张图片像素点颜色
img = cv2.imread(image_path)
# img = cv2.cvtColor(img,cv2.COLOR_RGB2GRAY)
print(img[100,100])

# Numpy是用于快速数组计算的优化库。因此，简单地访问每个像素值并对其进行修改将非常缓慢，因此不建议使用。
# Numpy数组方法array.item()和array.itemset())被认为更好，但是它们始终返回标量。如果要访问所有B，G，R值，则需要分别调用所有的array.item()。
# img[100:200,120:220] = [0,0,0]

# 访问 10,10,G 图像，建议优化方法
print(img.item(10,10,2))
img.itemset((10,10,2),100)
print(img.item(10,10,2))

# 图像数据类型
print(img.dtype)

# ROI 图像区域操作
head = img[100:200,120:220]
img[0:100, 0:100] = head 


# BGR 通道拆分 BGR可以单独处理
b,g,r = cv2.split(img)
# 处理完成之后可以再次合并
img = cv2.merge((b,g,r))
# 或者可以针对通道单独获取或者处理
change_img = img.copy()
b = change_img[:, :, 0]
change_img[:,:,0] = b+100
# 图像合并，注意入参是元组
img_merger = np.hstack((img,change_img))
cv2.imshow("img_merger",img_merger)


# 设置边框填充
BLUE = [255,0,0]
# top，bottom，left，right 边界宽度（以相应方向上的像素数为单位）
# cv.BORDER_CONSTANT - 添加恒定的彩色边框。该值应作为下一个参数给出。
# cv.BORDER_REFLECT - 边框将是边框元素的镜像，如下所示： fedcba | abcdefgh | hgfedcb
# **cv.BORDER_REFLECT_101**或 **cv.BORDER_DEFAULT**与上述相同，但略有变化，例如： gfedcb | abcdefgh | gfedcba
# **cv.BORDER_REPLICATE**最后一个元素被复制，像这样： aaaaaa | abcdefgh | hhhhhhh
# **cv.BORDER_WRAP**难以解释，它看起来像这样： cdefgh | abcdefgh | abcdefg
# value -边框的颜色，如果边框类型为**cv.BORDER_CONSTANT**
replicate = cv2.copyMakeBorder(img,10,10,10,10,cv2.BORDER_REPLICATE)
reflect = cv2.copyMakeBorder(img,10,10,10,10,cv2.BORDER_REFLECT)
reflect101 = cv2.copyMakeBorder(img,10,10,10,10,cv2.BORDER_REFLECT_101)
wrap = cv2.copyMakeBorder(img,10,10,10,10,cv2.BORDER_WRAP)
constant= cv2.copyMakeBorder(img,10,10,10,10,cv2.BORDER_CONSTANT,value=BLUE)

plt.subplot(231),plt.imshow(img,'gray'),plt.title('ORIGINAL')
plt.subplot(232),plt.imshow(replicate,'gray'),plt.title('REPLICATE')
plt.subplot(233),plt.imshow(reflect,'gray'),plt.title('REFLECT')
plt.subplot(234),plt.imshow(reflect101,'gray'),plt.title('REFLECT_101')
plt.subplot(235),plt.imshow(wrap,'gray'),plt.title('WRAP')
plt.subplot(236),plt.imshow(constant,'gray'),plt.title('CONSTANT')
plt.show()


cv2.imshow("img",img)

# 关闭窗口
k = cv2.waitKey(0)
if k == ord('q'):
    cv2.DestroyWindow("img")
    # cv2.destroyAllWindows()

