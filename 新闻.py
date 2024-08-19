# -*- codeing = utf-8
# @Time : 2022/10/28 11:47
# @Author : 钟
# @File : 新闻.py
# @Software: PyCharm
import numpy as np
from PIL import Image
import wordcloud
import jieba



def func1(c):
	file = open(c,"r",encoding="gbk")
	b=file.read()
	r=str(b)

	with open("c.txt","w") as f:
		f.write(r)


def main():
	c="新闻2.txt"
	func1(c)
if __name__ == "__main__":
    main()
    print("爬取完毕")
