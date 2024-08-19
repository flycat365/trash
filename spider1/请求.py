# -*- coding: utf-8 -*-


import requests

from flask import Flask, request
from bs4 import BeautifulSoup
app = Flask(__name__)


@app.route('/getInfo')
def hello_world():
    if(str(request.headers.get('User-Agent')).startswith('python')):
        return "小子，使用爬虫是吧？滚你的"
    else:
        return "这里假装有很多数据"


if __name__ == "__main__":
    app.run(debug=True)