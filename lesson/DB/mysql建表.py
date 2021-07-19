import pymysql

# 打开数据库连接
db = pymysql.connect(host="localhost", user="root", password="1qaz@WSX", database="sakila")
# 使用cursor()方法获取操作游标
cursor = db.cursor()
# SQL 更新语句
sql = "CREATE TABLE BAIDU_NEWS(NEW_RANK INT NOT NULL,TITLE CHAR(60) NOT NULL,CATEGORY CHAR(20) NOT NULL," \
      "CRAWLING_TIME DATETIME NOT NULL) "
try:
    # 执行SQL语句
    cursor.execute('DROP TABLE IF EXISTS BAIDU_NEWS')
    cursor.execute(sql)
except:
    # 发生错误时回滚
    print("发生错误时回滚")
    db.rollback()

# 关闭数据库连接
db.close()
