from selenium import webdriver
from time import sleep
from selenium.webdriver.common.keys import Keys
from tools.get_connect import DB
import time
import datetime
from datetime import datetime


def exp_db(db, localtime):
    # chrome选项
    options = webdriver.ChromeOptions()
    # 使用无头chrome(不打开页面，后台运行chrome)
    options.add_argument('headless')
    # chrome 的 webdriver驱动位置
    webdriver_path = "C:\Program Files (x86)\Google\Chrome\Application\chromedriver.exe"
    driver = webdriver.Chrome(executable_path=webdriver_path,
                              options=options)
    # 打开的网站
    driver.get("http://news.baidu.com/")
    driver.maximize_window()
    sleep(3)
    for i in range(0, 50):
        driver.find_element_by_tag_name('body').send_keys(Keys.ARROW_DOWN)  # 在这里使用模拟的下方向键
        sleep(0.1)

    with DB(host=db[0], user=db[1], password=db[2], database=db[3], port=db[4]) as cursor:
        i = int(1)
        hotword = {}
        while i <= 10:
            word = driver.find_element_by_xpath('//ul[@class="hotwords clearfix"]/li[' + str(i) + ']/a'). \
                get_attribute('title')
            hotword[i] = word
            print(hotword[i])
            # 使用预处理语句创建表
            sql = "INSERT INTO BAIDU_NEWS(NEWS_RANK,TITLE, CATEGORY,CRAWLING_TIME) VALUES (" \
                  + str(i) + ",'" + hotword[i] + "','新闻热搜词','" + localtime + "')"
            cursor.execute(sql)
            i += 1

    """
    # w+    打开一个文件用于读写。如果该文件已存在则打开文件，并从开头开始编辑，即原有内容会被删除。如果该文件不存在，创建新文件。
    with open(f, "w+") as hotwords:
        # 抓取10条新闻热搜词,每条按照左对齐 (宽度为2)依次写入文件，加上换行
        hotword = {}
        hotwords.write("新闻热搜词:" + '\n')
        i = int(1)
        while i <= 10:
            word = driver.find_element_by_xpath('//ul[@class="hotwords clearfix"]/li[' + str(i) + ']/a'). \
                get_attribute('title')
            hotword[i] = word
            hotwords.write("{0:<2} {1}".format(i, hotword[i]) + '\n')
            i += 1
    
        # 抓取5条（国内）热门点击,每条依次写入文件，加上换行
        hotword = {}
        hotwords.write('\n' + "国内热门点击:" + '\n')
        i = int(1)
        while i <= 5:
            word = driver.find_element_by_xpath('//*[@id="civil-aside-tophit"]/div[2]/ol/li[' + str(i) + ']/a'). \
                get_attribute('title')
            hotword[i] = word
            hotwords.write("{0:<2} {1}".format(i, hotword[i]) + '\n')
            i += 1
    
        # 抓取10条国际热搜词（网页左右各两列,注意格式化需要使用中文空格作为填充字符）,每条依次写入文件，加上换行
        hotword = {}
        hotwords.write('\n' + "国际热搜词:" + '\n')
        i = int(1)
        while i <= 5:
            word = driver.find_element_by_xpath('//*[@id="internal-hotword"]/div[2]/ol[1]/li[' + str(i) + ']/a'). \
                get_attribute('title')
            hotword[i] = word
            word = driver.find_element_by_xpath('//*[@id="internal-hotword"]/div[2]/ol[2]/li[' + str(i) + ']/a'). \
                get_attribute('title')
            hotword[i + 5] = word
            hotwords.write("{0:<2} {1:{4}<10} {2:<2} {3}".format(i, hotword[i], i + 5, hotword[i + 5], chr(12288)) + '\n')
            i += 1
    
        # 抓取5条（军事）热门点击,每条依次写入文件，加上换行
        hotwords.write('\n' + "军事热门点击:" + '\n')
        i = int(1)
        hotword = {}
        while i <= 5:
            word = driver.find_element_by_xpath('//*[@id="mil-aside-video"]/div[2]/ol/li[' + str(i) + ']/a'). \
                get_attribute('title')
            hotword[i] = word
            hotwords.write("{0:<2} {1}".format(i, hotword[i]) + '\n')
            i += 1
    
        # 读取文件里的内容并打印
        print("文件名为: ", hotwords.name)
        hotwords.seek(0, 0)  # 移动文件对象至第一个字符(之前write到了文件末尾)
        message = hotwords.read()
        print(message)
    """
    driver.quit()
