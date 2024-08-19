# -*-coding:utf-8-*-
# @Time : 2023/4/24 12:33
# @Author : 钟
# @File : 图像的平滑处理.py
# @Software: PyCharm
import cv2
import matplotlib.pyplot as plt
import numpy as np

img=cv2.imread('一张图片')
cv2.imshow('一张图片',img)
cv2.waitKey(0)
cv2.destroyAllWindows()
#图像的展示
#均值滤波
#对图像的处理，就是选择一个矩阵对里面矩阵求和相加，在除以矩阵大小，取取平均值作为数结果
blur=cv2.blur(img,(3,3))#首先用cv2中函数对图片选取3*3的矩阵，并进行卷积，滤波操作
cv2.imshow('blur',blur)
cv2.waitKey(0)
cv2.destroyAllWindows()
#方框滤波和均值滤波差不多
box=cv2.boxFilter(img,-1,(3,3),normalsize=True)#最后一项是进行归一化-1表示颜色通道为-1，通常不进行改变，最后一项就是归一化，就不会越界，造成全白的情况

cv2.imshow('box',box)
cv2.waitKey(0)
cv2.destroyAllWindows()
#高斯滤波和中值滤波，高斯函数就是正态分布函数和上面一样，靠近中间的权重增加，取中心值计算别的值和他的权重
#距离权重值越近发挥作用就越强
aussian=cv2.GaussiarBlur(img,(5,5),1)
cv2.imshow('aussian',aussian)
cv2.waitKey(0)
cv2.destroyAllWindows()
#中值滤波就是用中值替代，中值从小到大排序中间值就是中值，把中间那个作为处理结果

media=cv2.medianBlur(img,5)
cv2.imshow('media',media)
cv2.waitKey(0)
cv2.destroyAllWindows()
#对所有的进行展示
res=np.hstack(blur,aussian,media)#对图片进行链接，这个hstack是进行横向链接，vstack是进行竖向链接
cv2.imshow(res)
cv2.imshow('median',res)
cv2.waitKey(0)
cv2.destroyAllWindows()


