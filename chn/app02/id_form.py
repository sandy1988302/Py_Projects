from django import forms
from django.core.exceptions import ValidationError
# noinspection PyUnresolvedReferences
from app02 import models
from datetime import datetime


class AdminDivisionsForm(forms.Form):
    """
    根据〖中华人民共和国国家标准 GB 11643-1999〗中有关公民身份号码的规定，公民身份号码是特征组合码，由十七位数字本体码和一位数字校验码组成。
    排列顺序从左至右依次为：六位数字地址码，八位数字出生日期码，三位数字顺序码和一位数字校验码。
    """
    id_number = forms.CharField(max_length=18, min_length=15, label="身份证号码",
                                error_messages={"required": "请输入有效的身份证号码",
                                                "min_length": "请输入18位数的身份证号码",
                                                "max_length": "请输入18位数的身份证号码"})

    def clean_id_number(self):  # 局部钩子
        check_id = self.cleaned_data.get("id_number")
        if check_id.isdigit():
            print("都是数字" + check_id)
            return check_id
        elif check_id[17] == 'X' and check_id[:17].isdigit():
            print("最后一位是X，前17位是数字"+check_id)
            return check_id
        else:
            raise ValidationError("身份证为十七位数字本体码和一位数字校验码（最后一位为数字或者X）")

    def clean(self):  # 全局钩子
        check_id = self.cleaned_data.get("id_number")
        print(check_id)
        if len(check_id) != 18:
            raise ValidationError("请输入18位的身份证号码")

        """
        地址码（身份证前六位）表示编码对象常住户口所在县(市、旗、区)的行政区划代码。
        """
        admin_code = check_id[:6]
        try:
            ad = models.AdminDivisions.objects.get(code=admin_code)
        except:
            raise ValidationError("身份证前6位不是有效的行政区划代码")
        admin_name = ad.admin_name
        province_name = ad.province_name
        city_name = ad.city_name
        county_name = ad.county_name

        """
        生日期码（身份证第七位到第十四位）表示编码对象出生的年、月、日，其中年份用四位数字表示，年、月、日之间不用分隔符。
        """
        birthday_code = check_id[6:14]
        try:
            birthday = datetime.strptime(birthday_code, "%Y%m%d").date()
            print("登记的出生日期为%s" % birthday)
        except ValueError:
            raise ValidationError("身份证第七位到第十四位表示编码对象出生的年、月、日，其中年份用四位数字表示，年、月、日之间不用分隔符")

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
            raise ValidationError("第18位校验码(" + check_id[17] + ")不符合规则,应当为" + str(check_code))

        """
        顺序码（身份证第十五位到十七位）为同一地址码所标识的区域范围内，对同年、月、日出生的人员编定的顺序号。其中第十七位奇数分给男性，偶数分给女性。 
        """
        sex_code = int(check_id[16:17])
        if sex_code % 2 == 0:
            sex = '女性'
        else:
            sex = '男性'
        print("性别登记为%s" % sex)

        message = {"message": "输入的身份证为：%s,\n性别登记为%s,\n登记的出生日期为%s,\n出生地为%s,\n省级行政区划：%s,\n地级行政区划：%s,\n县级行政区划：%s" % (
            check_id, sex, birthday, admin_name, province_name, city_name, county_name)}

        return message
