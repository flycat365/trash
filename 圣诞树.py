 # �C coding: gbk �C
# @Time : 2022/10/18 18:52
# @Author : ��
# @File : 147.py
# @Software: PyCharm

import turtle as t
from turtle import *
import random as r
import time



n = 100.0
t.delay(0)
speed("fastest")
screensize(bg='black')
def bgpic(self, picname=None):
    if picname is None:
        return self._bgpicname
    if picname not in self._bgpics:
        self._bgpics[picname] = self._image(picname)
    self._setbgpic(self._bgpic, self._bgpics[picname])
    self._bgpicname = picname
if __name__ == '__main__':
    myWin = t.Screen()
    t.setup(width=600, height=750, startx=0, starty=0)
    t.bgpic('C:/Users/20447/Desktop/1671855651231.gif')


left(90)
forward(3*n)
color("orange", "yellow")
begin_fill()
left(126)
for i in range(5):
    forward(n/5)
    right(144)
    forward(n/5)
    left(72)
end_fill()
right(126)


def drawlight():
    if r.randint(0, 50) == 0:#������òʵ�̫�࣬���԰�ȡֵ��Χ�Ӵ�һЩ����Ӧ�ĵƾͻ���һЩ
        color('tomato')
        begin_fill()
        circle(6)
        end_fill()
    elif r.randint(0,50) == 1:
        color('orange')
        begin_fill()
        circle(3)
        end_fill()
    elif r.randint(0,50) == 2:
        color('pink')
        begin_fill()
        circle(2)
        end_fill()
    else:
        pensize(5)
        color('green')

pensize(5)
color("dark green")
backward(n*5)
def tree(d, s):
    if d <= 0: return
    forward(s)
    tree(d-1, s*.8)
    right(120)
    tree(d-3, s*.5)
    drawlight()#ͬʱ��С�ʵ�
    right(120)
    tree(d-3, s*.5)
    right(120)
    backward(s)
tree(15, n)
backward(n/2)

for i in range(200):
    a = 200 - 400 * r.random()
    b = 10 - 20 * r.random()
    up()
    forward(b)
    left(90)
    forward(a)
    down()
    if r.randint(0, 1) == 0:
        pensize(1)
        color('tomato')
    else:
        pensize(1)
        color('wheat')
    circle(2)
    up()
    backward(a)
    right(90)
    backward(b)

t.color("dark red","red")
t.write("ʥ������",align ="center",font=("Comic Sans MS",30,"bold"))
penup()
left(180)
backward(50)
pendown()
t.write("����",align ="center",font=("Comic Sans MS",30,"bold"))



def drawsnow():
    t.ht()  #���ر�ͷ��ht=hideturtle
    t.pensize(2)  #�����ͷ��С
    for i in range(200): #������ѩ��
        t.pencolor("white") #���廭����ɫΪ��ɫ����ʵ����ѩ��Ϊ��ɫ
        t.pu() #��ʣ�pu=penup
        t.setx(r.randint(-350,350)) #����x���꣬�����-350��350֮��ѡ��
        t.sety(r.randint(-100,350)) #����y���꣬ע��ѩ��һ���ڵ��ϲ������£����Զ����Ǵ�1��ʼ
        t.pd() #��ʣ�pd=pendown
        dens = 6 #ѩ��������Ϊ6
        snowsize = r.randint(1,10) #����ѩ����С
        for j in range(dens): #����6���Ǿ��ǻ�5�Σ�Ҳ����һ��ѩ�������
            #t.forward(int(snowsize))  #int����ȡ����
            t.fd(int(snowsize))

            t.backward(int(snowsize))
            #t.bd(int(snowsize))  #ע��û��bd=backward������fd=forward��Сbug
            t.right(int(360/dens))  #ת���Ƕ�

drawsnow()#��ѩ��
t.done()  # ���,�����ֱ�ӹر�
time.sleep(1)