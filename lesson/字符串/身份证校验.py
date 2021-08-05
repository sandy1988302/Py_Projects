import sys
from datetime import datetime
from tools.get_connect import DB

db = ("localhost", "root", "1qaz@WSX", "sakila", 3306)
"""
根据〖中华人民共和国国家标准 GB 11643-1999〗中有关公民身份号码的规定，公民身份号码是特征组合码，由十七位数字本体码和一位数字校验码组成。
排列顺序从左至右依次为：六位数字地址码，八位数字出生日期码，三位数字顺序码和一位数字校验码。 
"""
check_id = input('需要检查的18位身份证号码：')
if len(check_id) != 18:
    print('号码不是18位数字')
    sys.exit()
"""
校验码（身份证最后一位）是根据前面十七位数字码，按照ISO 7064:1983.MOD 11-2校验码计算出来的检验码。 
第十八位数字的计算方法为： 
1.将前面的身份证号码17位数分别乘以不同的系数。从第一位到第十七位的系数分别为：7 9 10 5 8 4 2 1 6 3 7 9 10 5 8 4 2 
2.将这17位数字和系数相乘的结果相加。 
3.用加出来和除以11，看余数是多少？ 
4余数只可能有0 1 2 3 4 5 6 7 8 9 10这11个数字。其分别对应的最后一位身份证的号码为1 0 X 9 8 7 6 5 4 3 2。 
5.通过上面得知如果余数是2，就会在身份证的第18位数字上出现罗马数字的Ⅹ。如果余数是10，身份证的最后一位号码就是2。 
"""
coefficient = [7, 9, 10, 5, 8, 4, 2, 1, 6, 3, 7, 9, 10, 5, 8, 4, 2]
s = 0
for i in range(0, 17):
    b = int(check_id[i]) * coefficient[i]
    s = s + b
    i += 1
remainder = s % 11
n = ['1', '0', 'X', '9', '8', '7', '6', '5', '4', '3', '2']
check_code = n[remainder]
if str(check_code) == check_id[17]:
    print("第18位校验码(" + str(check_code) + ")符合规则")
else:
    print("第18位校验码(" + check_id[17] + ")不符合规则,应当为"+str(check_code))
    sys.exit()
"""
地址码（身份证前六位）表示编码对象常住户口所在县(市、旗、区)的行政区划代码。
"""
admin_code = check_id[:6]
with DB(host=db[0], user=db[1], password=db[2], database=db[3], port=db[4]) as cursor:
    sql = "select ADMIN_NAME,PROVINCE_NAME,CITY_NAME,COUNTY_NAME from ADMIN_DIVISIONS where CODE='" + admin_code + "'"
    cursor.execute(sql)
    results = cursor.fetchall()
    for row in results:
        admin_name = row['ADMIN_NAME']
        province_name = row['PROVINCE_NAME']
        city_name = row['CITY_NAME']
        county_name = row['COUNTY_NAME']
        print("出生地为%s,省级行政区划：%s,地级行政区划：%s,县级行政区划：%s" % (admin_name, province_name, city_name, county_name))
"""
生日期码（身份证第七位到第十四位）表示编码对象出生的年、月、日，其中年份用四位数字表示，年、月、日之间不用分隔符。
"""
birthday_code = check_id[6:14]
birthday = datetime.strptime(birthday_code, "%Y%m%d").date()
print("登记的出生日期为%s" % birthday)
"""
顺序码（身份证第十五位到十七位）为同一地址码所标识的区域范围内，对同年、月、日出生的人员编定的顺序号。其中第十七位奇数分给男性，偶数分给女性。 
"""
sex_code = int(check_id[16:17])
if sex_code % 2 == 0:
    sex = '女性'
else:
    sex = '男性'
print("性别登记为%s" % sex)
