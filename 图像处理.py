
# @Time : 2023/4/17 18:28
# @Author : 钟
# @File : 图像处理.py
# @Software: PyCharm
from textwrap import wrap

import cv2
import matplotlib.pyplot as plt
import numpy as np

img=cv2.imread('D:/fu/22.jpg')
#print(img)
# cv2.imshow('1',img)
# cv2.waitKey(100)
# cv2.destroyAllWindows()
# print(img.shape)
def cv_show(name,img):
    cv2.imshow(name,img)
    cv2.waitKey(10000)
    cv2.destroyAllWindows()


img=cv2.imread('D:/fu/22.jpg',cv2.IMREAD_GRAYSCALE)
#print(img)
#截取部分图像
img=cv2.imread('D:/fu/22.jpg')
cat=img[20:200,0:200:3]
cv_show('cat',cat)
#颜色通道的提取
b,g,r=cv2.split(img)#进行颜色通道提取
#img=cv2.merge((b,g,r))#对其中的信息进行提取

print(img.shape)
#只保留R
cur_img=img.copy()
cur_img[:,:,0]=0#把b为0
cur_img[:,:,1]=0#把g为0
cv_show('R',cur_img)
#只保留G
cur_img=img.copy
cur_img[:,:,0]=0#把b为0

cur_img[:,:,2]=0#把r为0
cv_show('G',cur_img)

cur_img=img.copy()
cur_img[:,:,1]=0
cur_img[:,:,2]=0
cv_show('B',cur_img)
#边界填充
top_size,bottom_size,left_size,right_size=(50,50,50,50)
replicate=cv2.copyMakeBorder(img,top_size,bottom_size,left_size,right_size,borderType=cv2.BORDER_REPLICATE)#复制填充法
reflect=cv2.copyMakeBorder(img,top_size,bottom_size,left_size,right_size,cv2.BORDER_REFLECT)#反射填充法
reflect101=cv2.copyMakeBorder(img,top_size,bottom_size,left_size,right_size,cv2.BORDER_REFLECT_101)#反射填充边缘反射
# wrap=cv2.copyMakeBorder(img,top_size,bottom_size,left_size,right_size,cv2.BOEDER_WRAP)#外包装法，用外包装进行填充
constant=cv2.copyMakeBorder(img,top_size,bottom_size,left_size,right_size,cv2.BORDER_CONSTANT,value=0)#常量进行填充
import matplotlib.pyplot as plt
plt.subplot(231),plt.imshow(img,'gray'),plt.title('ORIGINAL')
plt.subplot(232),plt.imshow(replicate,'gray'),plt.title('REPLICATE')
plt.subplot(233),plt.imshow(reflect101,'gray'),plt.title('reflect101')
plt.subplot(234),plt.imshow(wrap,'gray'),plt.title('wrap')
plt.subplot(235),plt.imshow(constant,'gray'),plt.title('CONSTANT')
plt.show()
#数值计算
img_cat=cv2.imread('D:/fu/22.jpg')#进行加法运算是每一个数都要加10
img_dog=cv2.imread('C:/Users/20447/Pictures/131.jpg')
img_cat2=img_cat+10
print(img_cat[:5,:,0])#[:5,:,0]是用来限定打印行数
print(img_cat2[:5,:,0])
#两张图片维度相同才能进行相加
#相加规律就是各各点两个相加，当超出量程会越界会进行取余然后会以相加的结果减去最大边界加1作为结果
cv2.add(img_cat,img_cat2)[:,5:,0]#这个和上面的不同
#首先这个到达边界值时不会在相加取余只会留存最大的边界
#图像融合
#两张图片shape值不同时不能直接相加
#这时候可以把图片进行图片大小统一
#就是进行resize操作
img_dog=cv2.resize(img_dog,(500,414))#这里优先改的是宽度，然后才是高度
#shape值分别是高度，宽度，颜色通道
img_cat=cv2.resize(img_cat,(500,414))
res=cv2.resize(img,(0,0),fx=3,fy=1)#前面表示不变/后面的fx和fy分别指在x轴或者y轴方向进行拉伸，后面的数值表示拉伸的大小
plt.imshow(res)
res2=cv2.resize(img,(0,0),fx=1,fy=3)
plt.imshow(res2)
res3=cv2.addWeighted(img_cat,0.1,img_dog,0.1,0)#进行两张图片融合公式为R=ax1+bx2+c # 其中分别表示x1表示我输入的图片img_cat,其中的先
#x2表示我输入的另一个图片img_dog
#0.4和0.6分别为常数项#这里是存疑的
#最后一项b是用来提亮度的
plt.imshow(res3)

