import bs4
import time
from tools import get_html
from pyh import *


def exp_data():
    # 抓取热搜新闻词
    url = "http://news.baidu.com/"
    html = get_html.fetch_url(url)
    bsobj = bs4.BeautifulSoup(html, 'html.parser')
    hotwords_list = bsobj.find('ul', attrs={'class': 'hotwords clearfix'}).find_all('li')
    i = 1
    page = PyH('百度热搜')
    page << h1('新闻热搜词', cl='center')
    mytab = page << table()
    for hotword in hotwords_list:
        tr1 = mytab << tr()
        tr1 << td(str(i))
        td1 = tr1 << td()
        title = hotword.a["title"]
        mya = td1 << a(href=str("https://www.baidu.com/s?wd=" + title))
        mya << p(title)
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
    page << h1('国内热门点击', cl='center')
    mytab = page << table()
    for hotword in hotwords_list:
        tr1 = mytab << tr()
        tr1 << td(str(i))
        td1 = tr1 << td()
        title = hotword.a["title"]
        mya = td1 << a(href=str(hotword.a["href"]))
        mya << p(title)
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
    page << h1('国际热搜词', cl='center')
    mytab = page << table()
    for hotword in hotwords_list:
        tr1 = mytab << tr()
        tr1 << td(str(i))
        td1 = tr1 << td()
        title = hotword.a["title"]
        mya = td1 << a(href=str("http://news.baidu.com/ns?cl=2&ct=9&rn=20&sp=hotquery&word=" + title))
        mya << p(title)
        i += 1

    hotwords_list = bsobj.find('div', attrs={'id': 'internal-hotword'}).find('div', attrs={'class': 'bd'}) \
        .find('ol').next_sibling.next_sibling.find_all('li')
    i = 1
    for hotword in hotwords_list:
        tr1 = mytab << tr()
        tr1 << td(str(i + 5))
        td1 = tr1 << td()
        title = hotword.a["title"]
        mya = td1 << a(href=str("http://news.baidu.com/ns?cl=2&ct=9&rn=20&sp=hotquery&word=" + title))
        mya << p(title)
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
    page << h1('军事热门点击', cl='center')
    mytab = page << table()
    for hotword in hotwords_list:
        tr1 = mytab << tr()
        tr1 << td(str(i))
        td1 = tr1 << td()
        title = hotword.a["title"]
        mya = td1 << a(href=str(hotword.a["href"]))
        mya << p(title)
        i += 1

    # 抓取百度热搜
    url = "https://top.baidu.com/board?tab=realtime"
    html = get_html.fetch_url(url)
    bsobj = bs4.BeautifulSoup(html, 'html.parser')
    hotwords_list = bsobj.find_all('div', attrs={'class': 'c-single-text-ellipsis'})
    i = 1
    page << h1('百度热搜', cl='center')
    mytab = page << table()
    for hotword in hotwords_list:
        tr1 = mytab << tr()
        tr1 << td(str(i))
        td1 = tr1 << td()
        title = hotword.text.strip()
        if title[0] == '#' and title[-1] == '#':  # 热搜词加上了话题标签需要转义
            title = title.strip('#')
            mya = td1 << a(href=str("https://www.baidu.com/s?wd=%23" + title + "%23"))
            mya << p(title)
        else:
            mya = td1 << a(href=str("https://www.baidu.com/s?wd=" + title))
            mya << p(title)
        i += 1

    html = page.render()
    return html
