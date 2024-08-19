# -*- coding: utf-8 -*-
#定义代理
proxie = {
        'http' : 'http://xx.xxx.xxx.xxx:xxxx',
        'http' : 'http://xxx.xx.xx.xxx:xxx',
        ....
    }
#使用代理
response = requests.get(url,proxies=proxies)
#网上有代理ip，也可以用爬虫爬取作为IP池