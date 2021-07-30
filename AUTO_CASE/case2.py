import pandas as pd

# 三个字段 name, site, age
NEWS_RANK1 = [1, 2, 3, 4]
TITLE1 = ["习近平对防汛救灾工作作出重要指示", "习近平总书记西藏行", "全国11省区有大到暴雨", "汪顺获男子200米个人混合泳冠军"]
CATEGORY1 = ["新闻热搜词", "新闻热搜词", "新闻热搜词", "新闻热搜词"]
LINK1 = ["https://www.baidu.com/s?wd=习近平对防汛救灾工作作出重要指示", "https://www.baidu.com/s?wd=习近平总书记西藏行",
         "https://www.baidu.com/s?wd=全国11省区有大到暴雨", "https://www.baidu.com/s?wd=汪顺获男子200米个人混合泳冠军"]
NEWS_RANK2 = [1, 2, 3, 4]
TITLE2 = ["好事！大庆市民在商场、超市、医院、小区等地，扫码即..", "常平镇优秀共产党员夏忠平：从部队“老兵”到环保工作..", "一月之内山东两家公司上市，环保行业的戴维斯双击要来..",
          "县市区动态丨武城环保铁军闻“汛”而动   全力以赴.."]
CATEGORY2 = ["国内热门点击", "国内热门点击", "国内热门点击", "国内热门点击"]
LINK2 = ["http://baijiahao.baidu.com/s?id=1706609702681818757", "http://baijiahao.baidu.com/s?id=1706492513078393706",
         "http://baijiahao.baidu.com/s?id=1706517911061255981", "http://baijiahao.baidu.com/s?id=1706644945334991578"]
# 字典
NEWS_RANK1 += NEWS_RANK2
TITLE1 += TITLE2
CATEGORY1 += CATEGORY2
LINK1 += LINK2
dict1 = {'NEWS_RANK': NEWS_RANK1, 'TITLE': TITLE1, 'CATEGORY': CATEGORY1, 'LINK': LINK1}
df = pd.DataFrame(dict1)
# 保存 dataframe
df.to_csv('site.csv', encoding="utf_8_sig")
