# -*-coding:utf-8-*-
import re
import jieba
from wordcloud import WordCloud
import cv2.cv2 as cv


def analysis(savepath):
    f = open(savepath, 'r', encoding='utf-8')
    result = f.read()
    result = re.sub('[a-zA-Z0-9"#$%&\'()*+,-./:：;""（）<=>?@，。?、…【】《》？！[\\]^_`{|}~\s]+', '', result)
    jieba.add_word('人民至上')
    jieba.add_word('习近平主席')
    words = jieba.lcut(result)
    string = []
    for word in words:

        if len(word) == 1:
            continue
        else:
            string.append(word)

    strings =' '.join(string)
    mk = cv.imread('R-C.png')
    w = WordCloud(font_path="C:\Windows\Fonts\STFANGSO.TTF", background_color="white", width=1000, height=600, mask=mk,
                  max_words=50, colormap="autumn",
                  stopwords={'我们', '大家', '不同', '还有', '致以', '才能', '不负', '无论是', '实现', '只有', '一年', '历史', '世界', '意义','中共中央','今天','新华社','记者','年月日','中央军委','楷体','总书记'})
    w.generate(strings)
    w.to_file('wordcloud.jpg')
    image = w.to_image()
    image.show()


def main():
    savepath = "23.txt"
    analysis(savepath)
    print("finish")


if __name__ == "__main__":
    main()
