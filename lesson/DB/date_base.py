from datetime import datetime

from tools.get_connect import DB
import time
import datetime

if __name__ == '__main__':
    with DB(host="localhost", user="root", password="1qaz@WSX", database="sakila", port=3306) as cursor:
        # 使用预处理语句创建表
        localtime = time.asctime(time.localtime(time.time()))
        now = datetime.datetime.now()
        now_time = now.strftime('%Y-%m-%d %H:%M:%S')
        print(now_time)

        sql = "INSERT INTO BAIDU_NEWS(NEW_RANK,TITLE, CATEGORY,CRAWLING_TIME) VALUES " \
              "(1,'习近平：早日建成高水平亚太自由贸易区','新闻热搜词','"+now_time+"')"
        cursor.execute(sql)

        '''
        sql = "INSERT INTO BAIDU_NEWS (NEW_RANK,TITLE, CATEGORY,CRAWLING_TIME) VALUES (%s,%s,%s,%s)"
        val = [
            ('2', '构建中拉命运共同体 习主席这样领航前行', '新闻热搜词', now_time),
            ('3', '“矿都洼地”崛起“产业高地”——郴州资源型产业转型..', '国内热门点击', now_time),
            ('4', '印度外长访俄', '国际热搜词', now_time),
            ('5', '向3.5亿“无私无畏”的烟民“致敬”！', '军事热门点击', now_time)
        ]
        cursor.executemany(sql, val)
'''