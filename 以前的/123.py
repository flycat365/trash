
# �õ�һ��ָ����ҳ��URL
import re  # ����
# ��ҳ����
import xlwt  # excel
import urllib.request, urllib.error  # �ƶ�url��ȡ��������


from bs4 import BeautifulSoupdef getURL(url):
    hand = {          # ģ��������򶹰귢����Ϣ
        "User-Agent": "Mozilla/5.0(Windows NT 10.0;Win64;x64) AppleWebKit / 537.36(KHTML, like Gecko) Chrome / 111.0.0.0Safari / 537.36Edg / 111.0.1661.51"
    }
    request = urllib.request .Request(url, headers=hand)
    html = ''

    try:
        response = urllib.request.urlopen(request)
        html = response.read().decode("utf-8")

    except urllib.error.URLError as e:
        if hasattr(e, "code"):
            print(e.code)
        if hasattr(e, "reason"):
            print(e.reason)
# 1.��ȡ��ҳ



def getData(baseurl):
    datalist = []
    for i in range(0,10):
        url = baseurl + str(i*1)   #���ú���ҳ��ʮ��
        html = getURL(url)     #�����ȡ������ҳԴ��
        # 2.��������
        soup = BeautifulSoup(html,"html.parser")
        for item in soup.find_all('div',class_="item"):
            item = str(item)#���ҷ���Ҫ����ַ���



    return datalist
def getURL(url):
    hand = {          # ģ��������򶹰귢����Ϣ
        "User-Agent": "Mozilla/5.0(Windows NT 10.0;Win64;x64) AppleWebKit / 537.36(KHTML, like Gecko) Chrome / 111.0.0.0Safari / 537.36Edg / 111.0.1661.51"
    }
    request = urllib.request .Request(url, headers=hand)
    html = ''

    try:
        response = urllib.request.urlopen(request)
        html = response.read().decode("utf-8")

    except urllib.error.URLError as e:
        if hasattr(e, "code"):
            print(e.code)
        if hasattr(e, "reason"):
            print(e.reason)
# 1.��ȡ��ҳ


# 3.��������
#def saveData(savepath):
def main():
    baseurl = "https://movie.douban.com/top250?start="
    #��ȡ��ҳ
    datalist = getData(baseurl)
    #��������



if __name__ == "__main__":
    main()
