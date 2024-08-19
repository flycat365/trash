# -*- codeing = utf-8
# @Time : 2022/10/14 18:21
# @Author : 钟
# @File : xing.py
# @Software: PyCharm

from time import sleep
import requests


import re


class Baidu():

    def __init__(self):
        # 这里设置的初始网址是按照资讯内容的时间排序的，也可以按照热点或这焦点排序来爬取新闻
        self.start_url = 'https://www.baidu.com/s?tn=news&rtt=4&bsst=1&cl=2&wd={}'
        self.headers = {"User-Agent": "这里设置你自己浏览器的user-agent"}
        # 标题列表、时间列表、新闻内容的url列表
        self.title_list = []
        self.time_list = []
        self.content_url_list = []
        self.driver = webdriver.Chrome()

    def get_content_list(self, start, page):
        # 定位新闻内容的元素位置
        div_list = self.driver.find_elements_by_xpath('//div[@id="content_left"]')
        # for循环遍历主要是为了得到不同的文章标题、时间及内容url地址
        for div in div_list:
            for i in range(start, page):
                # 获取标题
                title = div.find_element_by_xpath("//div[@id={}]/h3[@class='c-title']/a".format(str(i + 1))).text
                # 获取时间
                time = div.find_element_by_xpath("//div[@id={}]//p".format(str(i + 1))).text
                # 获取新闻内容的url地址
                content_url = div.find_element_by_xpath(
                    "//div[@id={}]/h3[@class='c-title']/a".format(str(i + 1))).get_attribute('href')
                time = time.split('  ')[1]
                self.title_list.append(title)
                self.time_list.append(time)
                self.content_url_list.append(content_url)
            # 得到下一页的元素（这里一定要注意，因为如果没有后面的下一页的话会定位失败）
        element = self.driver.find_element_by_xpath("//p[@id='page']//a[@class='n'][text()='下一页>']")

        return title, time, content_url, element, (start + 10), (page + 10)

    # 存储文章内容
    def save_content(self, title_list, time_list, content_url_list):
        wb = workbook.Workbook()
        ws = wb.active
        ws.append(['新闻标题', '新闻时间', '新闻内容链接'])

        for i in range(len(self.title_list)):
            ws.append([self.title_list[i], self.time_list[i], self.content_url_list[i]])

        wb.save('你自己的文件路径.xlsx')

    # 请求网页，得到网页内容
    def get_html_text(self, url, headers):
        try:
            response = requests.get(url, headers=headers)
            response.raise_for_status()
            response.encoding = response.apparent_encoding
            return response.text
        except:
            return ""

    # 解析不同的网页内容，用正则匹配中文字符
    def parse_html(self, html_text):
        try:
            news_text = re.findall('[\u4e00-\u9fa5]|[，。?]', html_text)
            news_content = ''.join(news_text)
            return news_content
        except:
            pass

    # 得到文件内容，存储新闻内容
    def get_news_content(self, news_url_list, title_list):
        for i in range(len(news_url_list)):
            html_text = self.get_html_text(str(news_url_list[i]), self.headers)
            news_content = self.parse_html(html_text)
            # 这里需要修改成你自己的新闻内容保存路径(/Users/yupei/Desktop/news_content/)
            with open('你自己想要保存的路径位置' + title_list[i][:10] + '.txt', 'w') as f:
                f.write(news_content)
                f.close()

    def run(self):
        # 1、请求百度网页，输入想要查询的股票内容
        name = input("请输入你想要查找新闻名称:")
        start, page = 0, 10
        self.start_url = self.start_url.format(name)
        self.driver.get(self.start_url)
        sleep(2)
        # 注：这里每一页的定位元素的id不断变化，所以需要去获取每一页的页数

        # 2、请求完成后自动点击资讯内容，选择按时间排序,爬取股票资讯内容及时间点并获取网页内容的url地址,将资讯和时间存到excel中,url保存在list中
        title, time, content_url, element, start, page = self.get_content_list(start, page)

        # 3、点击下一页继续爬取内容
        try:
            while element is not None:
                element.click()
                sleep(2)
                title, time, content_url, element, start, page = self.get_content_list(start, page)
        except:
            print("网页到头啦!!!")

        # 4、存储相应的新闻标题、新闻时间、新闻内容url信息，输出为excel表格
        self.save_content(self.title_list, self.time_list, self.content_url_list)

        # 5、爬取到的url_list，遍历得到相应的内容
        self.get_news_content(self.content_url_list, self.title_list)


if __name__ == '__main__':
    Auto_Baidu = Baidu()
    Auto_Baidu.run()