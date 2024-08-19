# -*-coding:utf-8-*-
# @Time : 2023/4/24 13:38
# @Author : 钟
# @File : 腐蚀操作.py
# @Software: PyCharm
import cv2
import matplotlib.pyplot as plt
import numpy as np


img=cv2.imread('jdscfhl')
cv2.imshow('img',img)
cv2.waitKey(0)
cv2.destroyAllWindows()

kernel=np.ones((5,5),np.uint8)#(5,5)表示腐蚀范围
erosion=cv2.erode(img,kernel,iterations=1)#iterations=1迭代次数，就是进行腐蚀的次数，迭代次数越多就越小
cv2.imshow('erosion',erosion)
cv2.waitKey(0)
cv2.destroyAllWindows()
#对图片进行腐蚀，去掉多余部分
pie=cv2.imread('pie.png')
cv2.imshow('pie',pie)
cv2.waitKey(0)
cv2.destroyAllWindows()
#首先选取一个范围，当出现不同值时就进行腐蚀
kernel=np.ones((30,30),np.uint8)
erosion_1=cv2.erode(pie,kernel,iteration=1)
erosion_2=cv2.erode(pie,kernel,iteration=2)
erosion_3=cv2.erode(pie,kernel,iteration=3)
res=np.hstack((erosion_1,erosion_2,erosion_3))
cv2.imshow('res',res)
cv2.waitKey(0)
cv2.destroyAllWindows()
