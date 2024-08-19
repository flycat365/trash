# -*-coding:utf-8-*-
# @Time : 2023/4/24 13:38
# @Author : ��
# @File : ��ʴ����.py
# @Software: PyCharm
import cv2
import matplotlib.pyplot as plt
import numpy as np


img=cv2.imread('jdscfhl')
cv2.imshow('img',img)
cv2.waitKey(0)
cv2.destroyAllWindows()

kernel=np.ones((5,5),np.uint8)#(5,5)��ʾ��ʴ��Χ
erosion=cv2.erode(img,kernel,iterations=1)#iterations=1�������������ǽ��и�ʴ�Ĵ�������������Խ���ԽС
cv2.imshow('erosion',erosion)
cv2.waitKey(0)
cv2.destroyAllWindows()
#��ͼƬ���и�ʴ��ȥ�����ಿ��
pie=cv2.imread('pie.png')
cv2.imshow('pie',pie)
cv2.waitKey(0)
cv2.destroyAllWindows()
#����ѡȡһ����Χ�������ֲ�ֵͬʱ�ͽ��и�ʴ
kernel=np.ones((30,30),np.uint8)
erosion_1=cv2.erode(pie,kernel,iteration=1)
erosion_2=cv2.erode(pie,kernel,iteration=2)
erosion_3=cv2.erode(pie,kernel,iteration=3)
res=np.hstack((erosion_1,erosion_2,erosion_3))
cv2.imshow('res',res)
cv2.waitKey(0)
cv2.destroyAllWindows()
