import bs4
from tools import get_html
from datetime import datetime
from tools.get_connect import DB


file = "D:\Py_Projects\AUTO_CASE\\baidu_news.txt"
db = ("localhost", "root", "1qaz@WSX", "sakila", 3306)
now = datetime.now()
localtime = now.strftime('%Y-%m-%d %H:%M:%S')
print("启动爬取时间:", localtime)
url = "http://news.baidu.com/"
html = get_html.fetch_url(url)
bsobj = bs4.BeautifulSoup(html, 'html.parser')
hotwords_list = bsobj.find('ul', attrs={'class': 'hotwords clearfix'}).find_all('li')
link_list = []
i = 1
with DB(host=db[0], user=db[1], password=db[2], database=db[3], port=db[4]) as cursor:
    for hotword in hotwords_list:
        title = hotword.a["title"]
        link = "https://www.baidu.com/s?wd=" + title
        sql = "INSERT INTO BAIDU_NEWS(NEWS_RANK,TITLE, CATEGORY,CRAWLING_TIME,LINK) VALUES (" \
              + str(i) + ",'" + title + "','新闻热搜词','" + localtime + "','" + link + "')"
        cursor.execute(sql)
        i += 1

