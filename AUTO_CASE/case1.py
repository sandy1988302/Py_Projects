import datetime


def get_date_list(begin_date, end_date):
    """
    获取日期列表
    :param begin_date: 开始日期
    :param end_date: 结束日期
    :return: 开始日期和结束日期之间的日期列表
    """
    start = datetime.datetime.strptime(begin_date, "%Y%m%d")
    end = datetime.datetime.strptime(end_date, "%Y%m%d")

    data_list = []
    for d in gen_dates(start, (end - start).days):
        data_list.append(d)
    return data_list


def gen_dates(b_date, days):
    d = datetime.timedelta(days=1)
    for i in range(days):
        yield b_date + d * i


beginDate = input('请输入开始日期:')
endDate = input('请输入结束日期:')
data = get_date_list(beginDate, endDate)

for da in data:
    year = str(da.year)
    month = str(da.month) if da.month >= 10 else '0' + str(da.month)
    da = str(da.day) if da.day >= 10 else '0' + str(da.day)

    print("爬取完成：" + year + month + da)
