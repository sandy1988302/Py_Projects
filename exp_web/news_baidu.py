from selenium import webdriver
from time import sleep
from selenium.webdriver.common.keys import Keys


def exp_print(f, webdriver_path, options, open_mode):
    driver = webdriver.Chrome(executable_path=webdriver_path,
                              options=options)
    # 打开的网站
    driver.get("http://news.baidu.com/")
    driver.maximize_window()
    # 模拟页面滚动，使得页面动态生成完全
    for i in range(0, 100):
        driver.find_element_by_tag_name('body').send_keys(Keys.ARROW_DOWN)  # 在这里使用模拟的下方向键
        sleep(0.1)

    with open(f, open_mode) as hotwords:
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
            hotwords.write(
                "{0:<2} {1:{4}<10} {2:<2} {3}".format(i, hotword[i], i + 5, hotword[i + 5], chr(12288)) + '\n')
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

    driver.quit()
