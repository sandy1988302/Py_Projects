import bs4
import time
from tools import get_html
from datetime import datetime
from tools.get_connect import DB

db = ("localhost", "root", "1qaz@WSX", "sakila", 3306)
now = datetime.now()
localtime = now.strftime('%Y-%m-%d %H:%M:%S')
print("启动爬取时间:", localtime)
with DB(host=db[0], user=db[1], password=db[2], database=db[3], port=db[4]) as cursor:
    # 抓取热搜新闻词
    url = "http://news.baidu.com/"
    html = get_html.fetch_url(url)
    bsobj = bs4.BeautifulSoup(html, 'html.parser')
    hotwords_list = bsobj.find('ul', attrs={'class': 'hotwords clearfix'}).find_all('li')
    i = 1
    for hotword in hotwords_list:
        title = hotword.a["title"]
        link = "https://www.baidu.com/s?wd=" + title
        sql = "INSERT INTO BAIDU_NEWS(NEWS_RANK,TITLE, CATEGORY,CRAWLING_TIME,LINK) VALUES (" \
              + str(i) + ",'" + title + "','新闻热搜词','" + localtime + "','" + link + "')"
        cursor.execute(sql)
        i += 1

    # 抓取国内China 热门点击
    url = "http://news.baidu.com/widget"
    params = {
        'id': 'civilnews',
        't': str(int(round(time.time() * 1000)))
    }
    html = get_html.fetch_url(url, params)
    bsobj = bs4.BeautifulSoup(html, 'html.parser')
    hotwords_list = bsobj.find('div', attrs={'id': 'civil-aside-tophit'}).find('div', attrs={'class': 'bd'}) \
        .find('ol').find_all('li')
    i = 1
    for hotword in hotwords_list:
        title = hotword.a["title"]
        link = hotword.a["href"]
        sql = "INSERT INTO BAIDU_NEWS(NEWS_RANK,TITLE, CATEGORY,CRAWLING_TIME,LINK) VALUES (" \
              + str(i) + ",'" + title + "','国内热门点击','" + localtime + "','" + link + "')"
        cursor.execute(sql)
        i += 1

    # 抓取国际 World 热搜词
    params = {
        'id': 'InternationalNews',
        't': str(int(round(time.time() * 1000)))
    }
    html = get_html.fetch_url(url, params)
    bsobj = bs4.BeautifulSoup(html, 'html.parser')
    hotwords_list = bsobj.find('div', attrs={'id': 'internal-hotword'}).find('div', attrs={'class': 'bd'}) \
        .find('ol').find_all('li')
    i = 1
    for hotwords in hotwords_list:
        hotword = hotwords
        title = hotword.a["title"]
        link = "http://news.baidu.com/ns?cl=2&ct=9&rn=20&sp=hotquery&word=" + title
        sql = "INSERT INTO BAIDU_NEWS(NEWS_RANK,TITLE, CATEGORY,CRAWLING_TIME,LINK) VALUES (" \
              + str(i) + ",'" + title + "','国际热搜词','" + localtime + "','" + link + "')"
        cursor.execute(sql)
        i += 1

    hotwords_list = bsobj.find('div', attrs={'id': 'internal-hotword'}).find('div', attrs={'class': 'bd'}) \
        .find('ol').next_sibling.next_sibling.find_all('li')
    i = 1
    for hotwords in hotwords_list:
        hotword = hotwords
        title = hotword.a["title"]
        link = "http://news.baidu.com/ns?cl=2&ct=9&rn=20&sp=hotquery&word=" + title
        sql = "INSERT INTO BAIDU_NEWS(NEWS_RANK,TITLE, CATEGORY,CRAWLING_TIME,LINK) VALUES (" \
              + str(i + 5) + ",'" + title + "','国际热搜词','" + localtime + "','" + link + "')"
        cursor.execute(sql)
        i += 1

    # 抓取军事 Military 热门点击
    params = {
        'id': 'MilitaryNews',
        't': str(int(round(time.time() * 1000)))
    }
    html = get_html.fetch_url(url, params)
    bsobj = bs4.BeautifulSoup(html, 'html.parser')
    hotwords_list = bsobj.find('div', attrs={'id': 'mil-aside-video'}).find('div', attrs={'class': 'bd'}) \
        .find('ol').find_all('li')
    i = 1
    for hotword in hotwords_list:
        title = hotword.a["title"]
        link = hotword.a["href"]
        sql = "INSERT INTO BAIDU_NEWS(NEWS_RANK,TITLE, CATEGORY,CRAWLING_TIME,LINK) VALUES (" \
              + str(i) + ",'" + title + "','军事热门点击','" + localtime + "','" + link + "')"
        cursor.execute(sql)
        i += 1
