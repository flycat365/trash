# -*-coding:utf-8-*-
# @Time : 2023/4/24 17:12
# @Author : 钟
# @File : 膨胀操作.py
# @Software: PyCharm
#膨胀操作和腐蚀操作互为逆运算
import cv2
import matplotlib.pyplot as plt
import numpy as np

img=cv2.imread('一个文件')
cv2.imshow('img',img)
cv2.waitKey(0)
cv2.destroyAllWindows()
kernel=np.ones((3,3),np.unit8)
dige_erosion=cv2.erode(img,kernel,iterations=1)
dige_erosion=cv2.erode(img,kernel,iterations=1)
cv2.imshow('erosion',dige_erosion)
cv2.waitKey(0)
cv2.destroyAllWindows()

kernel=np.ones((3,3),np.uint8)
dige_dilate=cv2.dilate(dige_erosion,kernel,iterations=1)
cv2.imshow('dilate',dige_dilate)
cv2.waitKey(0)
cv2.destroyAllWindows()

pie=cv2.imread('pie,png')
kernel=np.ones((30,30),np.uint8)#np.ones将里面的数据设为1
dilate_1=cv2.dilate(pie,kernel,iterations=1)#cv2.dilate这个函数对其进行膨胀操作从左到右依次是目标图片，进行操作的内核就是图片矩阵，最后是膨胀次数
dilate_2=cv2.dilate(pie,kernel,iterations=2)
dilate_3=cv2.dilate(pie,kernel,iterations=3)
res=np.hstack((dilate_1,dilate_2,dilate_3))
cv2.imshow('res',res)
cv2.waitKey(0)
cv2.destroyAllWindows()
#膨胀和腐蚀为逆运算
