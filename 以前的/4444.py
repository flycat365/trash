﻿#- * - coding = utf - 8
# @Time : 2022/10/18 22:15
# @Author : 钟
# @File : 4444.py
# @Software: PyCharm
# -*- codeing = utf-8
# @Time : 2022/10/15 15:21
# @Author : 钟
# @File : top250.py
# @Software: PyCharm


import re  # 正则
# 网页解析
import xlwt  # excel
import urllib.request, urllib.error  # 制定url获取网络数据
import sqlite3

from bs4 import BeautifulSoup


def main():
    baseurl = "https://movie.douban.com/top250?start="
    askURL(baseurl)
    datalist = getData(baseurl)
    savepath = ".\\豆瓣电影Top250.xls"
    saveDate(datalist, savepath)


findLink = re.compile(r'<a href="(.*?)">')
findImgSrc = re.compile(r'<img(.*)alt=(.*)src="(.*?)">', re.S)
findTitle = re.compile(r'<span class="title">(.*)</span>')
findRating = re.compile(r'<span class="rating_num" property="v:average">(.*)</span>')
findJudge = re.compile(r'<span>(\d*)人评价</span>')
findInq = re.compile(r'<span class="inq">(.*)</span>')
findBd = re.compile(r'<p class="">(.*?)</p>', re.S)


def getData(baseurl):
    # 爬取
    datalist = []
    for i in range(0, 10):
        url = baseurl + str(i * 25)
        html = askURL(url)
        # 解析
        soup = BeautifulSoup(html, "html.parser")
        for item in soup.find_all('div', class_="item"):
            data = []
            item = str(item)
            link = re.findall(findLink, item)[0]
            data.append(link)
            imgSrc = re.findall(findImgSrc, item)[0]
            data.append(imgSrc)
            titles = re.findall(findTitle, item)
            if (len(titles) == 2):
                ctitle = titles[0]
                data.append(ctitle)
                otitle = titles[1].replace("/", "")
                data.append(otitle)
            else:
                data.append(titles[0])
                data.append('')
            rating = re.findall(findRating, item)[0]
            data.append(rating)
            judgeNum = re.findall(findJudge, item)[0]
            data.append(judgeNum)
            inq = re.findall(findInq, item)
            if len(inq) != 0:
                inq = inq[0].replace(".", "")
                data.append(inq)
            else:
                data.append(" ")
            bd = re.findall(findBd, item)[0]
            bd = re.sub('<br(\s+)?/>(\s+)?', " ", bd)
            bd = re.sub('/', "", bd)
            data.append(bd.strip())
            datalist.append(data)

    return datalist


def saveDate(datalist, savepath):  # 保存
    workbook = xlwt.Workbook(encoding="utf-8", style_compression=0)
    worksheet = workbook.add_sheet('表1', cell_overwrite_ok=True)
    col = ("电影详情链接", "图片链接", "电影中文名", "电影外国名", "评分", "评价数", "概况", "相关信息")
    for i in range(0, 8):
        worksheet.write(0, i, col[i])
    for i in range(0, 250):
        print("第%d条" % (i + 1))
        data = datalist[i]
        for j in range(0, 8):
            worksheet.write(i + 1, j, data[j])  # 行数,列数,数据

    workbook.save('豆瓣TOP250.xls')


def askURL(url):
    head = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/106.0.0.0 Safari/537.36 Edg/106.0.1370.42"
    }
    request = urllib.request.Request(url, headers=head)
    html = ""
    try:
        response = urllib.request.urlopen(request)
        html = response.read().decode("utf-8")

    except urllib.error.URLError as e:
        if hasattr(e, "code"):
            print(e.code)
        if hasattr(e, "reason"):
            print(e.reason)
    return html


if __name__ == "__main__":
    main()
    print("爬取完毕")
#
