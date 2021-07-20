import datetime


def gen_dates(b_date, days):
    delta = datetime.timedelta(days=1)
    for i in range(days):
        print("gen_dates:" + str(b_date + delta * i))
        return b_date + delta * i
# yield


d = 0
start = datetime.datetime.strptime('20201230', "%Y%m%d")
end = datetime.datetime.strptime('20210102', "%Y%m%d")
print("起始日期相差" + str((end - start).days) + "天")
data_list = []
for day in gen_dates(start, (end - start).days):
    data_list.append(day)
    print("增加1天，现有" + str(len(data_list)) + "天")
print("获得了data_list[]")
for da in data_list:
    year = str(da.year)
    month = str(da.month) if da.month >= 10 else '0' + str(da.month)
    day = str(da.day) if da.day >= 10 else '0' + str(da.day)
    d = d + 1
    print(year + month + day + "爬取完成，已爬取" + str(d) + "天")
