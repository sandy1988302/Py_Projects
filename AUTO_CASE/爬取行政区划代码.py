from exp_web import db_admin_divisions
from datetime import datetime
import threading
import time


# 数据库配置[ip,用户,密码,数据库,端口]
DB = ("localhost", "root", "1qaz@WSX", "sakila", 3306)


class MyThread(threading.Thread):
    def __init__(self, thread_id, name, time1):
        threading.Thread.__init__(self)
        self.threadID = thread_id
        self.name = name
        self.time = time1

    def run(self):
        print("开始线程：" + self.name)
        if self.name == 'saveDB_requests':
            db_admin_divisions.exp_db(DB)
            print("%s: %s完成使用requests的爬取，结果保存在数据库" % (self.name, time.ctime(time.time())))
        print("退出线程：" + self.name)


if __name__ == '__main__':
    now = datetime.now()
    localtime = now.strftime('%Y-%m-%d %H:%M:%S')
    print("启动爬取时间:", localtime)
    # 创建新线程
    thread1 = MyThread(1, "saveDB_requests", localtime)
    # 开启新线程
    thread1.start()
    thread1.join()
    print("退出主线程")
