# -*-coding:utf-8-*-
# @Time : 2023/4/18 19:21
# @Author : ��
# @File : ��Ƶ����.py
# @Software: PyCharm
import cv2
import matplotlib.pyplot as plt
import numpy as np

vc=cv2.VideoCapture('test.mp4')
if vc.isOpened():
    open,frame=vc.read()
else :
    open=False#�����Ƶ�Ƿ񱻴�

while open:#����Ƶ����һ֡һ֡�Ķ�ȡ
    ret,frame=vc.read()
    if frame is None:
        break
    if ret==True:
        gray=cv2.cvColor(frame,cv2.COLOR_BGR2GRAY)
        cv2.imshow('result',gray)
        if cv2.waitKey(10)&0xFF==23:#�������Ҫ�У�
            break
vc.release()
cv2.destroyAllWindows()


