from selenium import webdriver
from exp_web import db_news_baidu
from exp_web import db_top_baidu_realtime
from exp_web import data_news_baidu
from exp_web import data_top_baidu_realtime
from datetime import datetime
import pandas as pd
import threading
import time

# chrome选项
options = webdriver.ChromeOptions()
# 使用无头chrome(不打开页面，后台运行chrome)
options.add_argument('headless')
# chrome 的 webdriver驱动位置
WD_PATH = "C:\Program Files (x86)\Google\Chrome\Application\chromedriver.exe"
# 预备存储的文件
CSV = "D:\Py_Projects\AUTO_CASE\\csv_baidu.csv"
# 数据库配置[ip,用户,密码,数据库,端口]
DB = ("localhost", "root", "1qaz@WSX", "sakila", 3306)


class MyThread(threading.Thread):
    def __init__(self, thread_id, name, time1):
        threading.Thread.__init__(self)
        self.threadID = thread_id
        self.name = name
        self.time = time1

    def run(self):
        print("开始线程：" + self.name)
        if self.name == 'saveDB_selenium':
            db_news_baidu.exp_db(DB, self.time, WD_PATH, options)
            db_top_baidu_realtime.exp_db(DB, self.time, WD_PATH, options)
            print("%s: %s完成使用selenium的chrome webdriver的爬取，结果保存在数据库" % (self.name, time.ctime(time.time())))
        elif self.name == 'saveCSV_requests':
            news_rank = []
            titles = []
            category = []
            link = []
            dict1 = data_news_baidu.exp_data(news_rank, titles, category, link)
            news_rank = dict1['NEWS_RANK']
            titles = dict1['TITLE']
            category = dict1['CATEGORY']
            link = dict1['LINK']
            df = pd.DataFrame(data_top_baidu_realtime.exp_data(news_rank, titles, category, link))
            df.to_csv(CSV, encoding="utf_8_sig", index=False)
            print("%s: %s完成使用requests的爬取，结果保存在CSV文件" % (self.name, time.ctime(time.time())))
        print("退出线程：" + self.name)


if __name__ == '__main__':
    now = datetime.now()
    localtime = now.strftime('%Y-%m-%d %H:%M:%S')
    print("启动爬取时间:", localtime)
    # 创建新线程
    thread1 = MyThread(1, "saveDB_selenium", localtime)
    thread2 = MyThread(2, "saveCSV_requests", localtime)
    # 开启新线程
    thread1.start()
    thread2.start()
    thread1.join()
    thread2.join()
    print("退出主线程")
