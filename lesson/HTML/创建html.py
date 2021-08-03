from pyh import *

f = "D:\\Py_Projects\\lesson\\HTML\\a.html"
hotwordList = [{'NEWS_RANK': '1', 'TITLE': '我是一个兵｜中国军队是这样的',
                'LINK': 'https://www.baidu.com/s?wd=我是一个兵｜中国军队是这样的'},
               {'NEWS_RANK': '2', 'TITLE': '81秒火箭军最新宣传片',
                'LINK': 'https://www.baidu.com/s?wd=81秒火箭军最新宣传片'},
               {'NEWS_RANK': '3', 'TITLE': '31省区市新增本土确诊55例',
                'LINK': 'https://www.baidu.com/s?wd=31省区市新增本土确诊55例'}
               ]
page = PyH('百度热搜')
# page.addCSS('myStylesheet1.css', 'myStylesheet2.css')
# page.addJS('myJavascript1.js', 'myJavascript2.js')
page << h1('新闻热搜词', cl='center')
# page << div(cl='myCSSclass1 myCSSclass2', id='myDiv1') << p('I love PyH!', id='myP1')
mytab = page << table()
for i in hotwordList:
    tr1 = mytab << tr()
    tr1 << td(str(i['NEWS_RANK']))
    td1 = tr1 << td()
    mya = td1 << a(href=str(i["LINK"]))
    mya << p(str(i["TITLE"]))

# mydiv2 = page << div(id='myDiv2')
# mydiv2 << h2('A smaller title') + p('Followed by a paragraph.')
# page << div(id='myDiv3')
# page.myDiv3.attributes['cl'] = 'myCSSclass3'
# page.myDiv3 << p('Another paragraph')
html = page.render()
with open(f, "w", encoding="utf-8") as hotwords:
    hotwords.write(html)
