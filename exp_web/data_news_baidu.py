import bs4
import time
from tools import get_html


def exp_data(news_rank, titles, category, link):
    # 抓取热搜新闻词
    url = "http://news.baidu.com/"
    html = get_html.fetch_url(url)
    bsobj = bs4.BeautifulSoup(html, 'html.parser')
    hotwords_list = bsobj.find('ul', attrs={'class': 'hotwords clearfix'}).find_all('li')
    i = 1
    for hotword in hotwords_list:
        news_rank.append(i)
        category.append('新闻热搜词')
        title = hotword.a["title"]
        titles.append(title)
        link.append("https://www.baidu.com/s?wd=" + title)
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
        news_rank.append(i)
        category.append('国内热门点击')
        title = hotword.a["title"]
        titles.append(title)
        link.append(hotword.a["href"])
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
        news_rank.append(i)
        category.append('国际热搜词')
        title = hotword.a["title"]
        titles.append(title)
        link.append("http://news.baidu.com/ns?cl=2&ct=9&rn=20&sp=hotquery&word=" + title)
        i += 1

    hotwords_list = bsobj.find('div', attrs={'id': 'internal-hotword'}).find('div', attrs={'class': 'bd'}) \
        .find('ol').next_sibling.next_sibling.find_all('li')
    i = 1
    for hotword in hotwords_list:
        news_rank.append(i + 5)
        category.append('国际热搜词')
        title = hotword.a["title"]
        titles.append(title)
        link.append("http://news.baidu.com/ns?cl=2&ct=9&rn=20&sp=hotquery&word=" + title)
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
        news_rank.append(i)
        category.append('军事热门点击')
        title = hotword.a["title"]
        titles.append(title)
        link.append(hotword.a["href"])
        i += 1

    dicts = {'NEWS_RANK': news_rank, 'TITLE': titles, 'CATEGORY': category, 'LINK': link}
    return dicts
