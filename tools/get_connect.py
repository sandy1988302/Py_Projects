import pymysql


class DB:
    """
    功能：建立mysql连接，结合with实现自动close连接
    参数：host,port,database,user,password,charset
    """
    def __init__(self, host='localhost', port=3306, database='', user='root', password='root', charset='utf8'):
        # 建立连接
        self.conn = pymysql.connect(host=host, port=port, database=database, user=user, passwd=password,
                                    charset=charset)
        # 创建游标，操作设置为字典类型
        self.cur = self.conn.cursor(cursor=pymysql.cursors.DictCursor)

    def __enter__(self):
        # 返回游标
        return self.cur

    def __exit__(self, exc_type, exc_val, exc_tb):
        # 提交数据库并执行
        self.conn.commit()
        # 关闭游标
        self.cur.close()
        # 关闭数据库连接
        self.conn.close()
