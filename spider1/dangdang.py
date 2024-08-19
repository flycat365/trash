# -*- coding: utf-8 -*-



import requests
import re

def write_item_to_file(item):
    # Define how you want to write the item to a file
    # For example, writing to a text file line by line:
    with open('dangdang_books.txt', 'a', encoding='utf-8') as f:
        f.write(str(item) + '\n')

def main(page):
    url = 'http://bang.dangdang.com/books/fivestars/01.00.00.00.00.00-recent30-0-0-1-' + str(page)
    html = request_dandan(url)
    if html:
        items = parse_result(html)  # 解析过滤我们想要的信息
        for item in items:
            write_item_to_file(item)
            print(item)

def request_dandan(url):
    try:
        response = requests.get(url)
        if response.status_code == 200:
            return response.text
    except requests.RequestException as e:
        print(f"Error fetching {url}: {e}")
        return None

def parse_result(html):
    pattern = re.compile('<li>.*?list_num.*?(\d+).</div>.*?<img src="(.*?)".*?class="name".*?title="(.*?)">.*?class="star">.*?class="tuijian">(.*?)</span>.*?class="publisher_info">.*?target="_blank">(.*?)</a>.*?class="biaosheng">.*?<span>(.*?)</span></div>.*?<p><span\sclass="price_n">&yen;(.*?)</span>.*?</li>', re.S)
    items = re.findall(pattern, html)
    for item in items:
        yield {
            'range': item[0],
            'image': item[1],
            'title': item[2],
            'recommend': item[3],
            'author': item[4],
            'times': item[5],
            'price': item[6]
        }

if __name__ == "__main__":
    for i in range(1, 26):
        main(i)