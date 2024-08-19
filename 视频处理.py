# -*-coding:utf-8-*-
# @Time : 2023/4/18 19:21
# @Author : 钟
# @File : 视频处理.py
# @Software: PyCharm
import cv2
import matplotlib.pyplot as plt
import numpy as np

vc=cv2.VideoCapture('test.mp4')
if vc.isOpened():
    open,frame=vc.read()
else :
    open=False#检查视频是否被打开

while open:#打开视频进行一帧一帧的读取
    ret,frame=vc.read()
    if frame is None:
        break
    if ret==True:
        gray=cv2.cvColor(frame,cv2.COLOR_BGR2GRAY)
        cv2.imshow('result',gray)
        if cv2.waitKey(10)&0xFF==23:#后面必须要有：
            break
vc.release()
cv2.destroyAllWindows()


