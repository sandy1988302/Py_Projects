import bs4
from tools import get_html
from app02 import models


def exp_db():
    massage = models.AdminDivisions.objects.all().delete()
    # 2020年12月中华人民共和国县以上行政区划代码
    url = "http://www.mca.gov.cn/article/sj/xzqh/2020/20201201.html"
    # 参考 http://www.stats.gov.cn/tjsj/tjbz/tjyqhdmhcxhfdm/2020/index.html
    html = get_html.fetch_url(url)
    bsobj = bs4.BeautifulSoup(html, 'html.parser')
    tr_list = bsobj.find_all('tr', attrs={'style': 'mso-height-source:userset;height:14.25pt'})
    print('一共找到' + str(len(tr_list)) + '行数据')
    previous_code = ''
    province_name = ''
    city_name = ''
    county_name = ''
    for tr in tr_list:
        td_list = tr.find_all('td')
        code = td_list[1].get_text()
        if code == '':  # 有的区划可能和上一个区划是同一个code，网页里显示空白
            code = previous_code
        province_code = code[:2]
        city_code = code[2:4]
        county_code = code[4:]
        name = str(td_list[2].get_text())
        if name[1].isspace():  # 以两个空格开始的名称是县级区划
            province_name = province_name
            city_name = city_name
            county_name = name.strip()
        elif name[0].isspace():  # 以一个空格开始的名称是市级区划
            province_name = province_name
            city_name = name.strip()
            county_name = ''
        else:  # 没有空格开始的名称是省级区划
            province_name = name
            city_name = ''
            county_name = ''
        massage = models.AdminDivisions(code=code, admin_name=name.strip(), province_code=province_code,
                                        province_name=province_name, city_code=city_code, city_name=city_name,
                                        county_code=county_code, county_name=county_name)
        massage.save()
        previous_code = code
    return True
