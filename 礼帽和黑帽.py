# -*-coding:utf-8-*-
# @Time : 2023/4/24 21:37
# @Author : 钟
# @File : 礼帽和黑帽.py
# @Software: PyCharm

import cv2
import matplotlib.pyplot as plt
import numpy as np
#礼帽=原始输入减去开运算的结果
#黑帽=闭运算减去原始数据的结果
img=cv2.imread('dige.png')
tophat=cv2.morphologyEx(img,cv2.MORPH_TOPHAL,kernel)
#我这里没定义kenel
cv2.imshow('tophat',tophat)
cv2.waitKey(0)
cv2.destroyAllWindows()
#黑帽
img=cv2.imread('')
blackhat=cv2.morphologyEx(img,cv2.MORPH_BLACKHAT,kernel)
cv2.imshow('blackhat',blackhat)
cv2.waitKey(0)
cv2.destroyAllWindows()