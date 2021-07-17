"""
print("网站名：{name}, 地址 {url}".format(name="菜鸟教程", url="www.runoob.com"))

# 通过字典设置参数
site = {"name": "菜鸟教程", "url": "www.runoob.com"}
print("网站名：{name}, 地址 {url}".format(**site))

# 通过列表索引设置参数
my_list = ['菜鸟教程', 'www.runoob.com']
print("网站名：{0[0]}, 地址 {0[1]}".format(my_list))  # "0" 是必须的

"""

from selenium import webdriver
from time import sleep
from selenium.webdriver.common.keys import Keys

# chrome选项
options = webdriver.ChromeOptions()
# 使用无头chrome(不打开页面，后台运行chrome)
options.add_argument('headless')
# chrome 的 webdriver驱动位置
webdriver_path = "C:\Program Files (x86)\Google\Chrome\Application\chromedriver.exe"

# 预备存储的文件
f = "D:\Py_Projects\AUTO_CASE\\baidu_news.txt"

driver = webdriver.Chrome(executable_path=webdriver_path,
                          options=options)
# 打开的网站
driver.get("http://news.baidu.com/")
driver.maximize_window()
# 模拟页面滚动，使得页面动态生成完全
for i in range(0, 50):
    driver.find_element_by_tag_name('body').send_keys(Keys.ARROW_DOWN)  # 在这里使用模拟的下方向键
    sleep(0.1)

# 抓取10条国际热搜词（网页左右各两列）,每条依次写入文件，加上换行
hotword = {}
"""
# 抓取10条新闻热搜词,每条按照左对齐 (宽度为2)依次写入文件，加上换行
print("新闻热搜词:")
i = int(1)
while i <= 10:
    word = driver.find_element_by_xpath('//ul[@class="hotwords clearfix"]/li[' + str(i) + ']/a').get_attribute(
        'title')
    # print(str(i) + ' ' + word)
    hotword[i] = word
    print("{0:<2} {1}".format(i, hotword[i]))
    i += 1
"""
# 抓取10条国际热搜词（网页左右各两列）,每条依次写入文件，加上换行
print('\n' + "国际热搜词:" + '\n')
i = int(1)
while i <= 5:
    word = driver.find_element_by_xpath(
        '//*[@id="internal-hotword"]/div[2]/ol[1]/li[' + str(i) + ']/a').get_attribute(
        'title')
    hotword[i] = word
    word = driver.find_element_by_xpath(
        '//*[@id="internal-hotword"]/div[2]/ol[2]/li[' + str(i) + ']/a').get_attribute(
        'title')
    hotword[i + 5] = word
    print("{0:<2} {1:{4}<10} {2:<2} {3}".format(i, hotword[i], i + 5, hotword[i + 5], chr(12288)))
    i += 1

driver.close()
