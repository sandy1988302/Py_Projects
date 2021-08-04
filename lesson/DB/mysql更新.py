import pymysql

# 打开数据库连接
db = pymysql.connect(host="localhost", user="root", password="1qaz@WSX", database="sakila")
# 使用cursor()方法获取操作游标
cursor = db.cursor()
# SQL 更新语句
# sql = "UPDATE EMPLOYEE SET AGE = AGE + 1 WHERE SEX = '%c'" % ('M')
sql = "alter table ADMIN_DIVISIONS modify CODE VARCHAR(6) NOT NULL"
sql1 = "alter table ADMIN_DIVISIONS add PROVINCE_CODE VARCHAR(2),add PROVINCE_NAME VARCHAR(60)," \
       "add CITY_CODE VARCHAR(2),add CITY_NAME VARCHAR(60),add COUNTY_CODE VARCHAR(2),add COUNTY_NAME VARCHAR(60)"
try:
    # 执行SQL语句
    cursor.execute(sql)
    cursor.execute(sql1)
    # 提交到数据库执行
    db.commit()
except:
    # 发生错误时回滚
    db.rollback()

# 关闭数据库连接
db.close()
