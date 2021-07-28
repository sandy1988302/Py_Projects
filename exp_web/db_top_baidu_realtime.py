from selenium import webdriver
from time import sleep
from tools.get_connect import DB
from tools import get_element


def exp_db(db, localtime, webdriver_path, options):
    driver = webdriver.Chrome(executable_path=webdriver_path,
                              options=options)
    # 打开的网站
    driver.get("https://top.baidu.com/board?tab=realtime")
    driver.maximize_window()
    sleep(3)

    # 获取当前页面存在多少条(条数<=30)热搜新闻
    a = b = 0
    while a <= 30:
        xpath1 = "//div[@class=\"index_1Ew5p c-index-bg" + str(30 - a) + "\"]"
        if not get_element.get_element_exist(driver, xpath1):
            a = a + 1
        else:
            b = int(30 - a)
            a = a + 31

    with DB(host=db[0], user=db[1], password=db[2], database=db[3], port=db[4]) as cursor:
        # 抓取所有新闻热搜词
        i = int(1)
        while i <= b:
            word = driver.find_element_by_xpath(
                '//*[@id="sanRoot"]/main/div[2]/div/div[2]/div[' + str(i) + ']/div[2]/a/div[1]')
            word = word.text
            if word[0] == '#' and word[-1] == '#':  # 热搜词加上了话题标签需要转义
                word = word.strip('#')
                link = "https://www.baidu.com/s?wd=%23" + word + "%23"
            else:
                link = "https://www.baidu.com/s?wd=" + word
            sql = "INSERT INTO BAIDU_NEWS(NEWS_RANK,TITLE, CATEGORY,CRAWLING_TIME,LINK) VALUES (" \
                  + str(i) + ",'" + word + "','百度热搜','" + localtime + "','" + link + "')"
            cursor.execute(sql)
            i += 1

    driver.quit()
