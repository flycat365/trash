# -*- coding = utf-8
# @Time : 2022/12/31 19:25
# @Author : 钟
# @File : XINFW.py
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