# -*-coding:utf-8-*-
# @Time : 2023/4/24 12:33
# @Author : ��
# @File : ͼ���ƽ������.py
# @Software: PyCharm
import cv2
import matplotlib.pyplot as plt
import numpy as np

img=cv2.imread('һ��ͼƬ')
cv2.imshow('һ��ͼƬ',img)
cv2.waitKey(0)
cv2.destroyAllWindows()
#ͼ���չʾ
#��ֵ�˲�
#��ͼ��Ĵ�������ѡ��һ�������������������ӣ��ڳ��Ծ����С��ȡȡƽ��ֵ��Ϊ�����
blur=cv2.blur(img,(3,3))#������cv2�к�����ͼƬѡȡ3*3�ľ��󣬲����о�����˲�����
cv2.imshow('blur',blur)
cv2.waitKey(0)
cv2.destroyAllWindows()
#�����˲��;�ֵ�˲����
box=cv2.boxFilter(img,-1,(3,3),normalsize=True)#���һ���ǽ��й�һ��-1��ʾ��ɫͨ��Ϊ-1��ͨ�������иı䣬���һ����ǹ�һ�����Ͳ���Խ�磬���ȫ�׵����

cv2.imshow('box',box)
cv2.waitKey(0)
cv2.destroyAllWindows()
#��˹�˲�����ֵ�˲�����˹����������̬�ֲ�����������һ���������м��Ȩ�����ӣ�ȡ����ֵ������ֵ������Ȩ��
#����Ȩ��ֵԽ���������þ�Խǿ
aussian=cv2.GaussiarBlur(img,(5,5),1)
cv2.imshow('aussian',aussian)
cv2.waitKey(0)
cv2.destroyAllWindows()
#��ֵ�˲���������ֵ�������ֵ��С���������м�ֵ������ֵ�����м��Ǹ���Ϊ������

media=cv2.medianBlur(img,5)
cv2.imshow('media',media)
cv2.waitKey(0)
cv2.destroyAllWindows()
#�����еĽ���չʾ
res=np.hstack(blur,aussian,media)#��ͼƬ�������ӣ����hstack�ǽ��к������ӣ�vstack�ǽ�����������
cv2.imshow(res)
cv2.imshow('median',res)
cv2.waitKey(0)
cv2.destroyAllWindows()


