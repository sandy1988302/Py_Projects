import bs4
from tools import get_html


def exp_data(news_rank, titles, category, link):
    url = "https://top.baidu.com/board?tab=realtime"
    html = get_html.fetch_url(url)
    bsobj = bs4.BeautifulSoup(html, 'html.parser')
    hotwords_list = bsobj.find_all('div', attrs={'class': 'c-single-text-ellipsis'})
    i = 1
    for hotword in hotwords_list:
        news_rank.append(i)
        category.append('百度热搜')
        title = hotword.text.strip()
        titles.append(title)
        if title[0] == '#' and title[-1] == '#':  # 热搜词加上了话题标签需要转义
            title = title.strip('#')
            link.append("https://www.baidu.com/s?wd=%23" + title + "%23")
        else:
            link.append("https://www.baidu.com/s?wd=" + title)
        i += 1
    dicts = {'NEWS_RANK': news_rank, 'TITLE': titles, 'CATEGORY': category, 'LINK': link}
    return dicts
