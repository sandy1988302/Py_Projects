from exp_web import pyh_news_baidu


f = "D:\\Py_Projects\\lesson\\HTML\\a.html"
news_rank = []
titles = []
category = []
link = []
html = pyh_news_baidu.exp_data()
with open(f, "w", encoding="utf-8") as hotwords:
    hotwords.write(html)
