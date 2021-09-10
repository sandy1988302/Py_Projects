import random

from django.http import JsonResponse
from django.shortcuts import render, redirect
from django.db.models import Q
# noinspection PyUnresolvedReferences
from app02 import check_id, get_ad, models
# noinspection PyUnresolvedReferences
from app02.id_form import AdminDivisionsForm


def input_id(request):
    if request.method == "GET":
        form = AdminDivisionsForm()  # 初始化form对象
        return render(request, "id.html", {"form": form})
    else:
        form = AdminDivisionsForm(request.POST)  # 将数据传给form对象
        if form.is_valid():  # 进行校验
            data = form.cleaned_data
            request.encoding = 'utf-8'
            print(request.POST['idnumber'])
            message = data['message']
            return render(request, "id.html", {"form": form, 'rlt': message})
        else:  # 校验失败
            clear_errors = form.errors.get("__all__")  # 获取全局钩子错误信息
            return render(request, "id.html", {"form": form, "clear_errors": clear_errors})


def number(request):
    request.encoding = 'utf-8'
    print(request.POST['idnumber'])
    if request.POST['idnumber']:
        message = check_id.check(request.POST['idnumber'])
    else:
        message = '你提交了空表单'
    ctx = {'rlt': message}
    return render(request, "id.html", ctx)


def admindivisions(request):
    request.encoding = 'utf-8'
    get_ad.exp_db()
    return render(request, 'id.html')


def get_id(request):
    request.encoding = 'utf-8'
    if request.method == "POST":
        print("开始获取输入数据")
        province_name = request.POST['province']
        city_name = request.POST['city']
        county_name = request.POST['county']
        birthday_code = request.POST['birthday_code'].replace('-', '')
        print(birthday_code)
        sex = request.POST['sex']
        id_quantity = int(request.POST['id_quantity'])
        num_list = get_idnumber(province_name, county_name, birthday_code, sex, id_quantity)
        # print("num_list为"+str(num_list))
        return JsonResponse(num_list, safe=False)
    else:
        print("开始获取省份列表")
        all_province = models.AdminDivisions.objects.filter(city_code='00').filter(county_code='00').values(
            "province_name").distinct()
        return render(request, "get_id.html", {"province_info_list": all_province})


def get_city(request):
    print("开始获取地级市列表")
    request.encoding = 'utf-8'
    if request.method == "GET":
        province_name = request.GET.get('province')
        print("GET，获取现在选择的省级行政区:" + str(province_name))
        if province_name:
            data = list(
                models.AdminDivisions.objects.filter(province_name=province_name).values("city_name").distinct())
            # print(str(data))
            # city_name为空时（直辖市），设置city_name和province_name 一致
            if data[0]["city_name"] == '':
                if len(data) == 1:
                    data.append({'city_name': str(province_name)})
                    print(str(data))
    return JsonResponse(data, safe=False)


def get_county(request):
    print("开始获取县级市列表")
    request.encoding = 'utf-8'
    if request.method == "GET":
        city_name = request.GET.get('city')
        print("GET，获取现在选择的市级行政区:" + str(city_name))
        if city_name:
            data = list(
                models.AdminDivisions.objects.filter(city_name=city_name).values("county_name").distinct())
            # print(str(data))
            # city_name为空时（直辖市），使用province_name做查询条件
            if not data:
                data = list(
                    models.AdminDivisions.objects.filter(province_name=city_name).values("county_name").distinct())
                # print(str(data))
    return JsonResponse(data, safe=False)


def get_idnumber(province_name, county_name, birthday_code, sex, id_quantity):
    conditions = {'province_name': province_name, 'county_name': county_name}
    code = models.AdminDivisions.objects.filter(**conditions).values("code").distinct()
    admin_code = code[0]['code']
    # print(admin_code)
    idnumber_list = []
    while len(idnumber_list) < id_quantity:
        a = str(random.randint(100, 199))[1:]
        # print(a)
        if sex == 'male':
            b = str(random.choices([1, 3, 5, 7, 9])[0])
        else:
            b = str(random.choices([0, 2, 4, 6, 8])[0])
        # print(b)
        prenum = admin_code + birthday_code + a + b
        # print(prenum)
        c = get_check_code(prenum)
        idnumber_list.append(prenum + c)
    return idnumber_list


def get_check_code(check_id):
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
    check_code = str(n[remainder])
    return check_code
