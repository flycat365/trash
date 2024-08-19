# -*- codeing = utf-8
# @Time : 2022/10/18 18:52
# @Author : 钟
# @File : 147.py
# @Software: PyCharm

import re  # 正则
from bs4 import BeautifulSoup  # 网页解析
import urllib.request, urllib.error  # 制定url获取网络数据




def main():
    baseurl = "http://www.xinhuanet.com/"  #新闻总网站
    getData(baseurl)  # 函数调用
    #生成词云



findlink = re.compile(r'<a href="(.*?)" target="_blank">')  # 分网站链接
findword= re.compile(r'<p>(.*?)</p>')  # 内容





def getData(baseurl):
    # 爬取
    links = []
    url=baseurl
    html = askURL(url)

    #print(html)
    # 解析
    soup = BeautifulSoup(html, "html.parser")
    #print(soup)
    try:
        for item in soup.find_all('li',class_="clearfix"):
            data = []
            item = str(item)
            link=str(re.findall(findlink,item)[0])
            html=askURL(link)
            Soup=BeautifulSoup(html, "html.parser")
            Soup=str(Soup )
            word=str(re.findall(findword,Soup ))
            word=str(re.findall(r'[\u4e00-\u9fa5]',word))
            word=word.replace("'",'')
            word = word.replace(",", '')
            word = str(word.replace(" ", ''))
            with open("新闻.txt", "a+") as f:  # 写入txt
                f.write(word)
            links.append(data)
            for item1 in soup.find_all('div', class_="list-focus"):  # 最上面的四个新闻的网站
                data1 = []
                item1 = str(item1)
                link = str(re.findall(findlink, item1)[0])
                html = askURL(link)
                Soup1 = BeautifulSoup(html, "html.parser")  # 解析那四个
                Soup1 = str(Soup1)
                word = str(re.findall(findword, Soup1))
                word = str(re.findall(r'[\u4e00-\u9fa5]', word))  # 提取所有汉字
                word = word.replace("'", '')
                word = word.replace(",", '')
                word = str(word.replace(" ", ''))
            with open("新闻.txt", "a+") as f:#写入txt
                f.write(word)
            links.append(data1)
            for i in range(0, 300):
                url = baseurl
                html = askURL(url)
            for item2 in soup.find_all('li', class_="active"):  # 最上面的四个新闻的网站
                data2 = []
                item2 = str(item2)
                link = str(re.findall(findlink, item2)[0])
                html = askURL(link)
                Soup2 = BeautifulSoup(html, "html.parser")  # 解析那四个
                Soup2 = str(Soup2)
                word = str(re.findall(findword, Soup2))
                word = str(re.findall(r'[\u4e00-\u9fa5]', word))  # 提取所有汉字
                word = word.replace("'", '')
                word = word.replace(",", '')
                word = str(word.replace(" ", ''))
            with open("新闻1.txt", "a+") as f:#写入txt
                f.write(word)
            links.append(data2)
    except Exception as e:
        print(e)

    return







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