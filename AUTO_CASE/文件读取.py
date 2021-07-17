import os
import codecs
from selenium import webdriver
from time import sleep
from selenium.webdriver.common.keys import Keys


# 预备存储的文件
f = "D:\Py_Projects\AUTO_CASE\\baidu_news.txt"

# 读取文件里的内容并打印
'''
try:
    hotwords = open(f, "r")
    print("文件名为: ", hotwords.name)
    for line in hotwords:
        print(line, end='')
finally:
    if hotwords:
        hotwords.close()
'''
with open(f, "r") as hotwords:
    print("文件名为: ", hotwords.name)
    for line in hotwords.readlines():  # 依次读取每行
        line = line.strip()  # 去掉每行头尾空白
        print(line)
