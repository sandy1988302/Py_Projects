from selenium import webdriver
from exp_web import news_baidu, pyh_news_baidu, top_baidu_realtime, db_news_baidu, db_top_baidu_realtime, \
    data_news_baidu, data_top_baidu_realtime
from datetime import datetime
import pandas as pd

# chrome选项
options = webdriver.ChromeOptions()
# 使用无头chrome(不打开页面，后台运行chrome)
options.add_argument('headless')
# chrome 的 webdriver驱动位置
webdriver_path = "C:\Program Files (x86)\Google\Chrome\Application\chromedriver.exe"
# 预备存储的文件
TXT = "D:\\Py_Projects\\AUTO_CASE\\baidu_news.txt"
CSV = "D:\\Py_Projects\\AUTO_CASE\\csv_baidu.csv"
HTML = "D:\\Py_Projects\\AUTO_CASE\\baidu.html"
# 数据库配置[ip,用户,密码,数据库,端口]
db = ("localhost", "root", "1qaz@WSX", "sakila", 3306)

if __name__ == '__main__':
    print("t：爬取数据导出到TXT文件\nd：爬取数据保存在数据库\nc：爬取数据保存在CSV文件\nh：爬取数据保存在HTML文件\n")
    option = input('请输入【t/d/c/h】：')
    now = datetime.now()
    localtime = now.strftime('%Y-%m-%d %H:%M:%S')
    print("启动爬取时间:", localtime)
    if option in ['t', 'T']:
        print("爬取数据保存在TXT文件")
        with open(TXT, "w")as hotword:
            hotword.write("爬取热搜数据开始时间：" + localtime + '\n')
        news_baidu.exp_print(TXT, webdriver_path, options, "a")
        top_baidu_realtime.exp_print(TXT, webdriver_path, options, "a")
    elif option in ['d', 'D']:
        print("爬取数据保存在数据库")
        db_news_baidu.exp_db(db, localtime, webdriver_path, options)
        db_top_baidu_realtime.exp_db(db, localtime, webdriver_path, options)
    elif option in ['c', 'C']:
        print("爬取数据保存在CSV文件")
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
        # excel能够正确识别gb2312、gbk、gb18030或utf_8 with BOM,所以不能直接使用utf_8
        df.to_csv(CSV, encoding="utf_8_sig", index=False)
    elif option in ['h', 'H']:
        print("爬取数据保存在HTML文件")
        html = pyh_news_baidu.exp_data()
        with open(HTML, "w", encoding="utf-8") as hotwords:
            hotwords.write(html)
    else:
        print("没有执行有效操作。")
