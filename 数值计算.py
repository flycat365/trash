# -*-coding:utf-8-*-
# @Time : 2023/4/23 21:30
# @Author : ��
# @File : ��ֵ����.py
# @Software: PyCharm
import cv2
import matplotlib.pyplot as plt
import numpy as np
img_cat=cv2.imread('һ��ͼƬ�ļ�')
img_dog=cv2.imread('��һ��ͼƬ')
img_cat2=img_cat+10
img_cat[:5,:,0]
img_cat2[:5,:,0]
(img_cat+img_cat2)[:5,:,0]#[:5,:,0]��ʾֻ��ǰ5��
