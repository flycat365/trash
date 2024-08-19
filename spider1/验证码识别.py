# -*- coding: utf-8 -*-
#多噪声点的这个代码不用改可以直接识别，但是对无噪声的有识别错误。噪声优化就不研究了。代码放在后面。如果不行的话可以让人工智障识别。
try:
    from PIL import Image
except ImportError:
    import Image
import pytesseract

def convert_img(img,threshold):
    img = img.convert("L")  # 处理灰度
    pixels = img.load()
    for x in range(img.width):
        for y in range(img.height):
            if pixels[x, y] > threshold:
                pixels[x, y] = 255
            else:
                pixels[x, y] = 0
    return img

captcha = Image.open("图片/img3.png")

a=convert_img(captcha,150)
a.show()
result = pytesseract.image_to_string(a)
print(result)


