# -*- coding: utf-8 -*-

import requests

headers = {
    # 假装自己是浏览器
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/127.0.0.0 Safari/537.36 Edg/127.0.0.0',
    # 把你刚刚拿到的Cookie塞进来
    'Cookie': 'zh_choose=s;wordpress_logged_in_ae620d8c6cebb4af7ae36370fe025fc3=123zyl%7C1723222116%7C4aB93aGTlrKYsVvDJZcpi826MPlTTlp6SpHM9eJS5RA%7C68b55336918df461f99de0cb2a02a390ef2683545073d10f905e2077d617a576; PHPSESSID=afum1tfutnsken5rhnbiu4gb7n',

}

session = requests.Session()
response = session.get('https://xdlabc.top/50873.html', headers=headers)

print(response.text)