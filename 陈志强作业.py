# 得到一个指定网页的URL
# -*- coding: utf-8 -*-
import re  # 正则
# 网页解析
import xlwt  # excel
import urllib.request, urllib.error  # 制定url获取网络数据
import sqlite3

from bs4 import BeautifulSoup

def getURL(url):
    hand = {          # 模拟浏览器向豆瓣发送消息
        "User-Agent": "Mozilla/5.0(Windows NT 10.0;Win64;x64) AppleWebKit / 537.36(KHTML, like Gecko) Chrome / 111.0.0.0Safari / 537.36Edg / 111.0.1661.51"
    }
    request = urllib.request .Request(url, headers=hand)
    html = ''

    try:
        response = urllib.request.urlopen(request)
        html = response.read().decode("utf-8")

    except urllib.error.URLError as e:
        if hasattr(e, "code"):
            print(e.code)
        if hasattr(e, "reason"):
            print(e.reason)
# 1.爬取网页

def getData(baseurl):
    datalist = []
    for i in range(0,10):
        url = baseurl + str(i*1)   #调用函数页面十次
        html = getURL(url)     #保存获取到的网页源码
        # 2.解析数据
        soup = BeautifulSoup(html,"html.parser")
        for item in soup.find_all('div',class_="item"):
            item = str(item)#查找符合要求的字符串
            print(item)


    return datalist


# 3.保存数据
#def saveData(savepath):
def main():
    baseurl = "https://movie.douban.com/top250?start="
    #爬取网页
    datalist = getData(baseurl)
    #保存数据



if __name__ == "__main__":
    main()
