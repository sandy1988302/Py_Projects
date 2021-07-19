import pymysql

# 打开数据库连接
db = pymysql.connect(host="localhost", user="root", password="1qaz@WSX", database="mysql")
# 使用cursor()方法获取操作游标
cursor = db.cursor()
# SQL 查询语句
sql = "SELECT * FROM EMPLOYEE \
       WHERE INCOME > %s" % 1000
try:
    # 执行SQL语句
    cursor.execute(sql)
    # 获取所有记录列表
    results = cursor.fetchall()
    for row in results:
        firstname = row[0]
        lastname = row[1]
        age = row[2]
        sex = row[3]
        income = row[4]
        # 打印结果
        print("firstname=%s,lastname=%s,age=%s,sex=%s,income=%s" % (firstname, lastname, age, sex, income))
except:
    print("Error: unable to fetch data")

# 关闭数据库连接
db.close()
