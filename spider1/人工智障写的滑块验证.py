# -*- coding: utf-8 -*-
from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from bs4 import BeautifulSoup
import re
import requests
from PIL import Image
from io import BytesIO

# 启动WebDriver
driver = webdriver.Chrome()
WAIT = WebDriverWait(driver, 10)

# 访问目标网页
url = "http://example.com"  # 替换为目标网页URL
driver.get(url)

# 等待滑块元素可点击
slider = WAIT.until(EC.element_to_be_clickable(
    (By.CSS_SELECTOR, "#gc-box > div > div.gt_slider > div.gt_slider_knob.gt_show")))

# 解析网页源代码以获取背景图片和缺口图片的URL
bs = BeautifulSoup(driver.page_source, 'lxml')
bg_div = bs.find_all(class_='gt_cut_bg_slice')
fullbg_div = bs.find_all(class_='gt_cut_fullbg_slice')

# 获取缺口背景图片和背景图片的URL
bg_url = re.findall('background-image:\surl\("(.*?)"\)', bg_div[0].get('style'))[0].replace('webp', 'jpg')
fullbg_url = re.findall('background-image:\surl\("(.*?)"\)', fullbg_div[0].get('style'))[0].replace('webp', 'jpg')

# 下载图片
bg_image = requests.get(bg_url).content
fullbg_image = requests.get(fullbg_url).content

# 存储图片位置
bg_location_list = []
fullbg_location_list = []

for bg in bg_div:
    location = {}
    location['x'] = int(re.findall('background-position:\s(.*?)px\s(.*?)px;', bg.get('style'))[0][0])
    location['y'] = int(re.findall('background-position:\s(.*?)px\s(.*?)px;', bg.get('style'))[0][1])
    bg_location_list.append(location)

for fullbg in fullbg_div:
    location = {}
    location['x'] = int(re.findall('background-position:\s(.*?)px\s(.*?)px;', fullbg.get('style'))[0][0])
    location['y'] = int(re.findall('background-position:\s(.*?)px\s(.*?)px;', fullbg.get('style'))[0][1])
    fullbg_location_list.append(location)

# 合成图片
def merge_images(image_file, location_list):
    new_image = Image.new('RGB', (260, 116))
    upper_half_list = []
    down_half_list = []
    image = Image.open(image_file)

    for location in location_list:
        if location['y'] == -58:
            im = image.crop((abs(location['x']), 58, abs(location['x']) + 10, 116))
            upper_half_list.append(im)
        elif location['y'] == 0:
            im = image.crop((abs(location['x']), 0, abs(location['x']) + 10, 58))
            down_half_list.append(im)

    offset = 0
    for im in upper_half_list:
        new_image.paste(im, (offset, 0))
        offset += 10

    offset = 0
    for im in down_half_list:
        new_image.paste(im, (offset, 58))
        offset += 10

    return new_image

bg_image_file = BytesIO(bg_image)
fullbg_image_file = BytesIO(fullbg_image)
bg_Image = merge_images(bg_image_file, bg_location_list)
fullbg_Image = merge_images(fullbg_image_file, fullbg_location_list)

# 计算缺口偏移距离
def get_distance(bg_Image, fullbg_Image):
    threshold = 200
    for i in range(60, bg_Image.size[0]):
        for j in range(bg_Image.size[1]):
            bg_pix = bg_Image.getpixel((i, j))
            fullbg_pix = fullbg_Image.getpixel((i, j))
            r = abs(bg_pix[0] - fullbg_pix[0])
            g = abs(bg_pix[1] - fullbg_pix[1])
            b = abs(bg_pix[2] - fullbg_pix[2])
            if r + g + b > threshold:
                return i
    return None

distance = get_distance(bg_Image, fullbg_Image)
print('得到距离：%s' % str(distance))

# 模拟拖动滑块
knob = WAIT.until(EC.presence_of_element