import bs4
from tools import get_html
from tools import get_element

url = "https://top.baidu.com/board?tab=realtime"
html = get_html.fetch_url(url)
bsobj = bs4.BeautifulSoup(html, 'html.parser')
# 获取当前页面存在多少条(条数<=30)热搜新闻
a = b = 0
while a <= 30:
    if not get_element.check_element(bsobj, 'div', 'class', 'index_1Ew5p c-index-bg' + str(30 - a)):
        print("没有找到元素" + str(30 - a))
        a = a + 1
    else:
        b = 30 - a
        print("找到元素" + str(b))
        a = a + 31
