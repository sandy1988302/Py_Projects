from selenium import webdriver

options = webdriver.ChromeOptions()
options.add_argument('headless')
webdriver_path = "C:\Program Files (x86)\Google\Chrome\Application\chromedriver.exe"
f = "D:\Py_Projects\AUTO_CASE\\baidu_news.txt"
driver = webdriver.Chrome(executable_path=webdriver_path,
                          options=options)
driver.get("https://top.baidu.com/board?tab=realtime")
driver.maximize_window()


# noinspection PyBroadException
def get_element_exist(dr, element_xpath):
    element_exist = True
    try:
        # 尝试寻找元素，如若没有找到则会抛出异常
        element = dr.find_element_by_xpath(element_xpath)
        print(dr.find_element_by_xpath(element_xpath).get_attribute('value'))
        print(xpath1+"元素存在!!")
    except:
        print(xpath1+"元素不存在.")
        element_exist = False

    return element_exist


# 获取当前页面存在多少条热搜新闻
# //*[@id="sanRoot"]/main/div[2]/div/div[2]/div[28]/a/div[1]
# //*[@id="sanRoot"]/main/div[2]/div/div[2]/div[' + '30-a' + ']/a/div[1]
# index_1Ew5p c-index-bg29
# index_1Ew5p c-index-bg29
a = b = 0
while a <= 30:
    xpath1 = "//div[@class=\"index_1Ew5p c-index-bg"+str(30-a)+"\"]"
    if not get_element_exist(driver, xpath1):
        print('没有第' + str(30-a) + '条热搜新闻')
        a = a + 1
    else:
        b = int(30 - a)
        print('当前页面存在' + str(b) + '条热搜新闻')
        a = a + 31

with open(f, "w+") as hotwords:
    # 抓取所有的热搜标题
    hotword = {}
    hotwords.write("百度热搜:" + '\n')
    i = int(1)
    while i <= b:
        word = driver.find_element_by_xpath('//*[@id="sanRoot"]/main/div[2]/div/div[2]/div[' + str(i) +
                                            ']/div[2]/a').get_attribute('text')
        hotword[i] = word
        hotwords.write("{0:<2} {1}".format(i, hotword[i]) + '\n')
        i += 1

    # 读取文件里的内容并打印
    hotwords.seek(0, 0)  # 移动文件对象至第一个字符(之前write到了文件末尾)
    message = hotwords.read()
    print(message)

driver.quit()
