# -*-coding:utf-8-*-
# @Time : 2023/4/24 21:37
# @Author : ��
# @File : ��ñ�ͺ�ñ.py
# @Software: PyCharm

import cv2
import matplotlib.pyplot as plt
import numpy as np
#��ñ=ԭʼ�����ȥ������Ľ��
#��ñ=�������ȥԭʼ���ݵĽ��
img=cv2.imread('dige.png')
tophat=cv2.morphologyEx(img,cv2.MORPH_TOPHAL,kernel)
#������û����kenel
cv2.imshow('tophat',tophat)
cv2.waitKey(0)
cv2.destroyAllWindows()
#��ñ
img=cv2.imread('')
blackhat=cv2.morphologyEx(img,cv2.MORPH_BLACKHAT,kernel)
cv2.imshow('blackhat',blackhat)
cv2.waitKey(0)
cv2.destroyAllWindows()