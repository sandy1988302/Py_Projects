from selenium import webdriver
from time import sleep
from selenium.webdriver.common.keys import Keys
from tools.get_connect import DB


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
    for i in range(0, 150):
        driver.find_element_by_tag_name('body').send_keys(Keys.ARROW_DOWN)  # 在这里使用模拟的下方向键
        sleep(0.1)

    with DB(host=db[0], user=db[1], password=db[2], database=db[3], port=db[4]) as cursor:
        # 抓取10条新闻热搜词
        i = int(1)
        hotword = {}
        while i <= 10:
            word = driver.find_element_by_xpath('//ul[@class="hotwords clearfix"]/li[' + str(i) + ']/a'). \
                get_attribute('title')
            hotword[i] = word
            sql = "INSERT INTO BAIDU_NEWS(NEWS_RANK,TITLE, CATEGORY,CRAWLING_TIME) VALUES (" \
                  + str(i) + ",'" + hotword[i] + "','新闻热搜词','" + localtime + "')"
            cursor.execute(sql)
            i += 1

        # 抓取5条（国内）热门点击
        i = int(1)
        hotword = {}
        while i <= 5:
            word = driver.find_element_by_xpath('//*[@id="civil-aside-tophit"]/div[2]/ol/li[' + str(i) + ']/a'). \
                get_attribute('title')
            hotword[i] = word
            sql = "INSERT INTO BAIDU_NEWS(NEWS_RANK,TITLE, CATEGORY,CRAWLING_TIME) VALUES (" \
                  + str(i) + ",'" + hotword[i] + "','国内热门点击','" + localtime + "')"
            cursor.execute(sql)
            i += 1

        # 抓取10条国际热搜词(左右各5条)
        i = int(1)
        hotword = {}
        while i <= 5:
            word = driver.find_element_by_xpath('//*[@id="internal-hotword"]/div[2]/ol[1]/li[' + str(i) + ']/a'). \
                get_attribute('title')
            hotword[i] = word
            sql = "INSERT INTO BAIDU_NEWS(NEWS_RANK,TITLE, CATEGORY,CRAWLING_TIME) VALUES (" \
                  + str(i) + ",'" + hotword[i] + "','国际热搜词','" + localtime + "')"
            cursor.execute(sql)
            i += 1

        i = int(1)
        hotword = {}
        while i <= 5:
            word = driver.find_element_by_xpath('//*[@id="internal-hotword"]/div[2]/ol[2]/li[' + str(i) + ']/a'). \
                get_attribute('title')
            hotword[i + 5] = word
            sql = "INSERT INTO BAIDU_NEWS(NEWS_RANK,TITLE, CATEGORY,CRAWLING_TIME) VALUES (" \
                  + str(i + 5) + ",'" + hotword[i + 5] + "','国际热搜词','" + localtime + "')"
            cursor.execute(sql)
            i += 1

        # 抓取5条（军事）热门点击
        i = int(1)
        hotword = {}
        while i <= 5:
            word = driver.find_element_by_xpath('//*[@id="mil-aside-video"]/div[2]/ol/li[' + str(i) + ']/a'). \
                get_attribute('title')
            hotword[i] = word
            sql = "INSERT INTO BAIDU_NEWS(NEWS_RANK,TITLE, CATEGORY,CRAWLING_TIME) VALUES (" \
                  + str(i) + ",'" + hotword[i] + "','军事热门点击','" + localtime + "')"
            cursor.execute(sql)
            i += 1

    driver.quit()
