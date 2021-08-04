import pymysql

# 打开数据库连接
db = pymysql.connect(host="localhost", user="root", password="1qaz@WSX", database="sakila")
# 使用cursor()方法获取操作游标
cursor = db.cursor()
# SQL 删除语句
# sql = "DELETE FROM BAIDU_NEWS WHERE NEWS_RANK > %s" % 0
# sql = "TRUNCATE BAIDU_NEWS"
sql = "TRUNCATE ADMIN_DIVISIONS"
try:
    # 执行SQL语句
    cursor.execute(sql)
    # 提交修改
    db.commit()
except:
    # 发生错误时回滚
    db.rollback()

# 关闭连接
db.close()
