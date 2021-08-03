import xml.dom.minidom

# 在内存中创建一个空的文档
doc = xml.dom.minidom.Document()
# 创建一个根节点Managers对象
root = doc.createElement('html')
# 将根节点添加到文档对象中
doc.appendChild(root)
hotwordList = [{'NEWS_RANK': '1', 'TITLE': '我是一个兵｜中国军队是这样的',
                'LINK': 'https://www.baidu.com/s?wd=我是一个兵｜中国军队是这样的'},
               {'NEWS_RANK': '2', 'TITLE': '81秒火箭军最新宣传片',
                'LINK': 'https://www.baidu.com/s?wd=81秒火箭军最新宣传片'},
               {'NEWS_RANK': '3', 'TITLE': '31省区市新增本土确诊55例',
                'LINK': 'https://www.baidu.com/s?wd=31省区市新增本土确诊55例'}
               ]
for i in hotwordList:
    nodebody = doc.createElement('body')
    nodeNews = doc.createElement('News')
    nodeNews.setAttribute('FROM', 'http://news.baidu.com/')
    nodeNews.setAttribute('CATEGORY', '新闻热搜词')
    nodeHotwords = doc.createElement('Hotwords')
    nodeNEWS_RANK = doc.createElement('NEWS_RANK')
    # 给叶子节点name设置一个文本节点，用于显示文本内容
    nodeNEWS_RANK.appendChild(doc.createTextNode(str(i['NEWS_RANK'])))
    nodeTITLE = doc.createElement("a")
    nodeTITLE.setAttribute('href', str(i["LINK"]))
    nodeTITLE.appendChild(doc.createTextNode(str(i["TITLE"])))
    # 将各叶子节点添加到父节点Manager中，
    # 最后将Manager添加到根节点Managers中
    root.appendChild(nodebody)
    nodebody.appendChild(nodeNews)
    nodeNews.appendChild(nodeHotwords)
    nodeHotwords.appendChild(nodeNEWS_RANK)
    nodeHotwords.appendChild(nodeTITLE)
# 开始写xml文档
with open('d:\\Py_Projects\\lesson\\XML\\Baidu_News.html', 'w', encoding="utf_8") as fp:
    doc.writexml(fp, indent='\t', addindent='\t', newl='\n', encoding="utf_8")
