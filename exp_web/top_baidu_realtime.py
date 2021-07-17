from selenium import webdriver
from tools import get_element


def exp_print(f, webdriver_path, options, open_mode):
    driver = webdriver.Chrome(executable_path=webdriver_path,
                              options=options)
    # 打开的网站
    driver.get("https://top.baidu.com/board?tab=realtime")
    driver.maximize_window()
    # 获取当前页面存在多少条(条数<=30)热搜新闻
    a = b = 0
    while a <= 30:
        xpath1 = "//div[@class=\"index_1Ew5p c-index-bg"+str(30-a)+"\"]"
        if not get_element.get_element_exist(driver, xpath1):
            a = a + 1
        else:
            b = int(30 - a)
            # print('当前页面存在' + str(b) + '条热搜新闻')
            a = a + 31

    with open(f, open_mode) as hotwords:
        # 抓取所有的热搜标题
        hotword = {}
        hotwords.write('\n'+"百度热搜:" + '\n')
        i = int(1)
        while i <= b:
            word = driver.find_element_by_xpath('//*[@id="sanRoot"]/main/div[2]/div/div[2]/div[' + str(i) +
                                                ']/div[2]/a').get_attribute('text')
            hotword[i] = word
            hotwords.write("{0:<2} {1}".format(i, hotword[i]) + '\n')
            i += 1

    driver.quit()
