import bs4
from tools import get_html
from tools.get_connect import DB


def exp_db(db):
    # 2020年12月中华人民共和国县以上行政区划代码
    url = "http://www.mca.gov.cn/article/sj/xzqh/2020/20201201.html"
    # 参考 http://www.stats.gov.cn/tjsj/tjbz/tjyqhdmhcxhfdm/2020/index.html
    html = get_html.fetch_url(url)
    bsobj = bs4.BeautifulSoup(html, 'html.parser')
    tr_list = bsobj.find_all('tr', attrs={'style': 'mso-height-source:userset;height:14.25pt'})
    print('一共找到' + str(len(tr_list)) + '行数据')
    previous_code = ''
    with DB(host=db[0], user=db[1], password=db[2], database=db[3], port=db[4]) as cursor:
        for tr in tr_list:
            td_list = tr.find_all('td')
            # print(len(td_list))
            code = td_list[1].get_text()
            if code == '':  # 有的区划可能和上一个区划是同一个code，网页里显示空白
                code = previous_code
            # print('code:' + code)
            admin_name = td_list[2].get_text().strip()
            # print('admin_name:' + admin_name)
            sql = "INSERT INTO ADMIN_DIVISIONS(CODE,ADMIN_NAME) VALUES (" + code + ",\'" + str(admin_name) + "\')"
            cursor.execute(sql)
            previous_code = code
