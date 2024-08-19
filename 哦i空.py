# -*- codeing = utf-8
# @Time : 2022/11/1 13:59
# @Author : ��
# @File : Ŷi��.py
# @Software: PyCharm
import requests
import re

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/85.0.4183.83 Safari/537.36'}
url = 'https://www.baidu.com/s?tn=news&rtt=1&bsst=1&cl=2&wd=����Ͱ�'  # ��������rtt��������4���ǰ�ʱ������Ĭ��Ϊ1����������
res = requests.get(url, headers=headers).text  # ����headers����������վ����ͨ��һ����������еķ���

"""ʹ��������ʽ��ȡ��Ϣ"""
# ��ȡ��Ϣ������
p_href = '<h3 class="news-title_1YtI1">< a href=" "'
href = re.findall(p_href, res)

# ��ȡ��Ϣ�ı���
p_title = '<h3 class="news-title_1YtI1">.*?>(.*?)</ a>'
title = re.findall(p_title, res, re.S)

# ��ȡ��Ϣ����Դ
p_source = '<span class="c-color-gray c-font-normal c-gap-right" aria-label=.*?>(.*?)</span>'
source = re.findall(p_source, res)

# ��ȡ��Ϣ������
p_date = '<span class="c-color-gray2 c-font-normal" aria-label=".*?>(.*?)</span>'
date = re.findall(p_date, res)

for i in range(len(title)):  # range(len(title)),������Ϊ֪��len(title) = 10������Ҳ����д��for i in range(10)
    title[i] = title[i].strip()  # strip()��������ȡ���ַ������˵Ļ��л��߿ո񣬲����������̫��Ҫ��
    title[i] = re.sub('<.*?>', '', title[i])  # ���ģ���re.sub()�������滻����Ҫ������
    print(str(i + 1) + '.' + title[i], source[i], date[i])  # print(1, 'hello') ����д����������ͬһ��������ӡ�������
    # print(str(i + 1) + '.' + title[i] + ' ' + source[i] + ' ' + date[i])  # ����Ǵ��ַ���ƴ��
    print(href[i])  # �������