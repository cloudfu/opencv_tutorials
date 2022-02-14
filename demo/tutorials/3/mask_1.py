#! /usr/bin/env python
# -*- coding: utf-8 -*-
 
import numpy as np
import cv2
 
# 因为是颜色，取值范围[0, 255], 类型应该为unsigned int 8 bit, 即uint8
# 可以把src1, src2看成一个像素点
# OpenCV中颜色顺序为BGR
src1 = np.array([[192, 0, 3]], dtype="uint8")
src2 = np.array([[162, 0, 34]], dtype="uint8")  # 红色
 
dst_and = cv2.bitwise_and(src1, src2)   # 按位与AND运算
dst_or = cv2.bitwise_or(src1, src2)     # 按位或OR运算
dst_xor = cv2.bitwise_xor(src1, src2)   # 按位异或XOR运算
dst_not_src1 = cv2.bitwise_not(src1)    # 按位否NOT运算
dst_not_src2 = cv2.bitwise_not(src2)    # 按位否NOT运算
# dst_and: [[128   0   2]]
# dst_or: [[226   0  35]]
# dst_xor: [[98  0 33]]
# dst_not_src1: [[ 63 255 252]]
# dst_not_src2: [[ 93 255 221]]


# 打印src1, src2的shape【可以理解为矩阵的维数】与内容
print("src1.shape:{}, src1:{}".format(src1.shape, src1))
print("src2.shape:{}, src2:{}".format(src2.shape, src2))
# src1.shape:(1, 3), src1:[[192   0   3]]
# src2.shape:(1, 3), src2:[[162   0  34]]

# 输出以上的按位运算结果
print("dst_and:",dst_and)
print("dst_or:",dst_or)
print("dst_xor:",dst_xor)
print("dst_not_src1:",dst_not_src1)
print("dst_not_src2:",dst_not_src2)
 
# 构建一个mask
# mask = np.array([[8, 46, 84]])    # not right
# mask = np.array([8,46,84])        # not right
# mask = np.array([[8]])            # not right
# 注意：以上几种写法都不对
 
# 正确写法如下：
mask = np.array([[231, 0, 0]], dtype="uint8")  # right, 一定要加dtype="uint8"
# mask = np.zeros((1,3), dtype="uint8")   # right，mask都为零
# mask = np.ones((1,3), dtype="uint8")      # right，mask都为一
 
# mask只能是二维的，单通道；因为这里src1.shape是二维的（1*3），所以我们可以这么写
# mask = np.zeros(src1.shape, dtype="uint8")    # right，mask都为零。
 
# 打印mask的shape与内容
print("mask.shape:{}, mask:{}".format(mask.shape, mask) )
# mask.shape:(1, 3), mask:[[231   0   0]]
#  
# mask运算
# 先按位与操作AND，再进行mask操作
and_mask = cv2.bitwise_and(src1, src2, mask=mask)
# 先按位或操作OR，再进行mask操作
or_mask = cv2.bitwise_or(src1, src2, mask=mask)
print("and_mask:", and_mask)
print("or_mask:",or_mask)
# and_mask: [[128   0   0]]
# or_mask: [[226   0   0]]