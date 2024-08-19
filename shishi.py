# -*-coding:utf-8-*-
# @Time : 2023/3/26 22:17
# @Author : 钟
# @File : shishi.py
# @Software: PyCharm
import urllib.request,urllib.error  # 制定URL，获取网页数据
def getURL(url):
    head = {          # 模拟浏览器向豆瓣发送消息
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/106.0.0.0 Safari/537.36 Edg/106.0.1370.42"
    }
    request=urllib.request.Request(url,headers=head)
    html =""

    try:
        response = urllib.request.urlopen(request)
        html = response.read().decode("gbk")
    except urllib.error.URLError as e:
        if hasattr(e, "code"):
            print(e.code)
        if hasattr(e, "reason"):
            print(e.reason)
            return  html
def main():
    baseurl="https://movie.douban.com/top250?start="
    getURL(baseurl)
if __name__ == "__main__":
    main()
    print(4)