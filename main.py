from selenium import webdriver
from exp_web import news_baidu
from exp_web import top_baidu_realtime
from exp_web import db_news_baidu
from exp_web import db_top_baidu_realtime
from datetime import datetime

# chrome选项
options = webdriver.ChromeOptions()
# 使用无头chrome(不打开页面，后台运行chrome)
options.add_argument('headless')
# chrome 的 webdriver驱动位置
webdriver_path = "C:\Program Files (x86)\Google\Chrome\Application\chromedriver.exe"
# 预备存储的文件
file = "D:\Py_Projects\AUTO_CASE\\baidu_news.txt"
# 数据库配置[ip,用户,密码,数据库,端口]
db = ("localhost", "root", "1qaz@WSX", "sakila", 3306)


def exp(a):
    # 导出"http://news.baidu.com/"的热搜标题
    now = datetime.now()
    localtime = now.strftime('%Y-%m-%d %H:%M:%S')
    print("启动爬取时间:", localtime)
    if a == 'f':
        # f：爬取数据导出到文件
        with open(file, "w")as hotword:
            hotword.write("爬取热搜数据开始时间：" + localtime + '\n')
        news_baidu.exp_print(file, webdriver_path, options, "a")
        top_baidu_realtime.exp_print(file, webdriver_path, options, "a")
    elif a == 'd':
        # d：爬取数据保存在数据库
        print("爬取数据保存在数据库")
        db_news_baidu.exp_db(db, localtime, webdriver_path, options)
        db_top_baidu_realtime.exp_db(db, localtime, webdriver_path, options)
    else:
        print("没有执行有效操作。输入f：爬取数据导出到文件 或者d：爬取数据保存在数据库")


# 按间距中的绿色按钮以运行脚本。
if __name__ == '__main__':
    exp('f')
