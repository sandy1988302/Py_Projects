from selenium import webdriver
from exp_web import news_baidu
from exp_web import top_baidu_realtime
import time

# chrome选项
options = webdriver.ChromeOptions()
# 使用无头chrome(不打开页面，后台运行chrome)
options.add_argument('headless')
# chrome 的 webdriver驱动位置
webdriver_path = "C:\Program Files (x86)\Google\Chrome\Application\chromedriver.exe"
# 预备存储的文件
f = "D:\Py_Projects\AUTO_CASE\\baidu_news.txt"


def exp(a):
    # 导出"http://news.baidu.com/"的热搜标题
    localtime = time.asctime(time.localtime(time.time()))
    print(a, ":", localtime)
    with open(f, "w")as hotword:
        hotword.write("爬取热搜数据开始时间：" + localtime + '\n')
    news_baidu.exp_print(f, webdriver_path, options, "a")
    top_baidu_realtime.exp_print(f, webdriver_path, options, "a")


# 按间距中的绿色按钮以运行脚本。
if __name__ == '__main__':
    exp('start')
