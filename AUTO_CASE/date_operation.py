from tools import get_days

beginDate = input('请输入开始日期:')
endDate = input('请输入结束日期:')
data = get_days.get_date_list(beginDate, endDate)
d = 0
for da in data:
    year = str(da.year)
    month = str(da.month) if da.month >= 10 else '0' + str(da.month)
    day = str(da.day) if da.day >= 10 else '0' + str(da.day)
    d = d + 1
    print(year + month + day + "爬取完成，已爬取" + str(d) + "天")


