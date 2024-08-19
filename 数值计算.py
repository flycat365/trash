# -*-coding:utf-8-*-
# @Time : 2023/4/23 21:30
# @Author : 钟
# @File : 数值计算.py
# @Software: PyCharm
import cv2
import matplotlib.pyplot as plt
import numpy as np
img_cat=cv2.imread('一个图片文件')
img_dog=cv2.imread('另一个图片')
img_cat2=img_cat+10
img_cat[:5,:,0]
img_cat2[:5,:,0]
(img_cat+img_cat2)[:5,:,0]#[:5,:,0]表示只打前5行
