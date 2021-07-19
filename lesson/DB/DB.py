import pymysql


class DB:
    def __init__(self, host='localhost', port=3306, database='', user='root', password='root', charset='utf8'):
        # 建立连接
        self.conn = pymysql.connect(host=host, port=port, database=database, user=user, passwd=password,
                                    charset=charset)
        # 创建游标，操作设置为字典类型
        self.cur = self.conn.cursor(cursor=pymysql.cursors.DictCursor)

    def __enter__(self):
        # 返回游标
        print("调用enter")
        return self.cur

    def __exit__(self, exc_type, exc_val, exc_tb):
        # 提交数据库并执行
        print("调用前面返回对象的exit")
        self.conn.commit()
        # 关闭游标
        self.cur.close()
        # 关闭数据库连接
        self.conn.close()


if __name__ == '__main__':
    with DB(host="localhost", user="root", password="1qaz@WSX", database="sakila", port=3306) as db:
        db.execute('select * from actor')
        print(db)
        for i in db:
            print(i)
