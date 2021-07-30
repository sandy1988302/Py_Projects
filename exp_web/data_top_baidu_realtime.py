import bs4
import time
from tools import get_html


def exp_data(news_rank, titles, category, link):
    url = "https://top.baidu.com/board?tab=realtime"
    html = get_html.fetch_url(url)
    bsobj = bs4.BeautifulSoup(html, 'html.parser')

    # 获取当前页面存在多少条(条数<=30)热搜新闻
    a = b = 0
    while a <= 30:
        xpath1 = "//div[@class=\"index_1Ew5p c-index-bg" + str(30 - a) + "\"]"
        if not get_element.get_element_exist(driver, xpath1):
            a = a + 1
        else:
            b = int(30 - a)
            a = a + 31