# -*- coding: utf-8 -*-
# @Time : 2023/4/23 21:42
# @Author : 钟
# @File : 阈值和平滑处理.py
# @Software: PyCharm
import cv2
import matplotlib.pyplot as plt
import numpy as np



# ret,dest=cv2.threshold(src,thresh,maxvel,type )
# src//输入图
# dst:输出图
# thresh:阈值
# maxvel:最大阈值当超出一定范围给他的值
# type：二指化的操作类型
# 主要有以下五种
# cv2.THRESH_BINARY超过阈值部分取最大值，否则维0
# cv2.THRESH_BINRAY_INV THRESH_BINARY的反转，亮度的反转
# cv2.THRESH_TRUNC大于阈值部分设为阈值，否则不变
# cv2.THRESH_TOZERO大于阈值部分不改变，否则为0
# cv2.THRESH_TOZERO_INV THRESH_TOZERO的反转
img=cv2.imread('D:/fu/22.jpg')
img_gray=img
ret,thresh1=cv2.threshold(img_gray,127,255,cv2.THRESH_BINARY)
ret,thresh2=cv2.threshold(img_gray,127,255,cv2.THRESH_BINARY_INV)
ret,thresh3=cv2.threshold(img_gray,127,255,cv2.THRESH_TRUNC)
ret,thresh4=cv2.threshold(img_gray,127,255,cv2.THRESH_TOZERO)
ret,thresh5=cv2.threshold(img_gray,127,255,cv2.THRESH_TOZER_INV)
titles=['Original Image','BINARY','BINARY_INV','TRUNC','TOZREO','TOZERO_INV']
imges=[img,thresh1,thresh2,thresh3,thresh4,thresh5]
for i in range(6):
            plt.subplot(2,3,i+1),plt.imshow(imges[i],'gray')
            plt.title(titles[i])
            plt.xticks([]),plt.yticks([])
plt.show()
#图像的平滑处理
