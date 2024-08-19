# -*- coding: utf-8 -*-

from selenium import webdriver
from selenium.webdriver.common.by import By

# 实例化Edge WebDriver
driver = webdriver.Edge()

# 打开网页
driver.get("http://www.baidu.com")

# 找到元素
element = driver.find_element(By.CSS_SELECTOR, '#kw')

# 做一些操作，例如输入内容
element.send_keys("你好，世界！")

# 关闭浏览器
