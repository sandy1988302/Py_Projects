import bs4
import time
from tools import get_html
from app01 import models


def exp_data(localtime):
    # 抓取热搜新闻词
    url = "http://news.baidu.com/"
    html = get_html.fetch_url(url)
    bsobj = bs4.BeautifulSoup(html, 'html.parser')
    hotwords_list = bsobj.find('ul', attrs={'class': 'hotwords clearfix'}).find_all('li')
    i = 1
    for hotword in hotwords_list:
        title = hotword.a["title"]
        link = "https://www.baidu.com/s?wd=" + title
        massage = models.BaiduNews(title=title, news_rank=i, category='新闻热搜词', crawling_time=localtime, link=link)
        massage.save()
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
        massage = models.BaiduNews(title=title, news_rank=i, category='国内热门点击', crawling_time=localtime, link=link)
        massage.save()
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
    for hotword in hotwords_list:
        title = hotword.a["title"]
        link = "http://news.baidu.com/ns?cl=2&ct=9&rn=20&sp=hotquery&word=" + title
        massage = models.BaiduNews(title=title, news_rank=i, category='国际热搜词', crawling_time=localtime, link=link)
        massage.save()
        i += 1

    hotwords_list = bsobj.find('div', attrs={'id': 'internal-hotword'}).find('div', attrs={'class': 'bd'}) \
        .find('ol').next_sibling.next_sibling.find_all('li')
    i = 1
    for hotword in hotwords_list:
        title = hotword.a["title"]
        link = "http://news.baidu.com/ns?cl=2&ct=9&rn=20&sp=hotquery&word=" + title
        massage = models.BaiduNews(title=title, news_rank=i + 5, category='国际热搜词', crawling_time=localtime, link=link)
        massage.save()
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
        massage = models.BaiduNews(title=title, news_rank=i, category='军事热门点击', crawling_time=localtime, link=link)
        massage.save()
        i += 1

    url = "https://top.baidu.com/board?tab=realtime"
    html = get_html.fetch_url(url)
    bsobj = bs4.BeautifulSoup(html, 'html.parser')
    hotwords_list = bsobj.find_all('div', attrs={'class': 'c-single-text-ellipsis'})
    i = 1
    for hotword in hotwords_list:
        title = hotword.text.strip()
        if title[0] == '#' and title[-1] == '#':  # 热搜词加上了话题标签需要转义
            ti = title.strip('#')
            link = "https://www.baidu.com/s?wd=%23" + ti + "%23"
        else:
            link = "https://www.baidu.com/s?wd=" + title
        massage = models.BaiduNews(title=title, news_rank=i, category='百度热搜', crawling_time=localtime, link=link)
        massage.save()
        i += 1
    return True
