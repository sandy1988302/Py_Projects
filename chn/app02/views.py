from django.http import JsonResponse
from django.shortcuts import render, redirect
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


# def province(request):
#     print("开始获取province_code与province_name")
#     request.encoding = 'utf-8'
#     all_province = models.AdminDivisions.objects.filter(city_code='00').filter(county_code='00')
#     province_info_list = [(prov.province_code, prov.province_name) for prov in all_province]
#     return JsonResponse(province_info_list, safe=False)


def get_city(request):
    print("开始获取地级市列表")
    request.encoding = 'utf-8'
    if request.method == "GET":
        province_name = request.GET.get('province')
        print("GET，获取现在选择的省份:"+str(province_name))
        if province_name:
            data = list(
                models.AdminDivisions.objects.filter(province_name=province_name).values("city_name"))
            return JsonResponse(data, safe=False)


def get_id(request):
    request.encoding = 'utf-8'
    if request.method == "POST":
        pass
    else:
        print("开始获取省份列表")
        all_province = models.AdminDivisions.objects.filter(city_code='00').filter(county_code='00').values(
            "province_name").distinct()
        return render(request, "get_id.html", {"province_info_list": all_province})
