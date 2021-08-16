from django.shortcuts import HttpResponse, render, redirect
from datetime import datetime
# noinspection PyUnresolvedReferences
from app01 import get_news, models
# noinspection PyUnresolvedReferences
from app01.My_forms import EmpForm
from django.core.exceptions import ValidationError
from django.db.models import Avg, Max, Min, Count, Sum


def start(request):
    return render(request, 'start.html')


def crawler(request):
    request.encoding = 'utf-8'
    now = datetime.now()
    localtime = now.strftime('%Y-%m-%d %H:%M:%S')
    print(localtime)
    get_news.exp_data(localtime)
    return HttpResponse('OK')


def add_book(request):
    res = models.Publish.objects.values("name").annotate(in_price=Min("book__price"))
    print(res)
    return HttpResponse(res)


def add_emp(request):
    if request.method == "GET":
        form = EmpForm()  # 初始化form对象
        return render(request, "add_emp.html", {"form": form})
    else:
        form = EmpForm(request.POST)  # 将数据传给form对象
        if form.is_valid():  # 进行校验
            data = form.cleaned_data
            data.pop("r_salary")
            models.Emp.objects.create(**data)
            return redirect("/index/")
        else:  # 校验失败
            clear_errors = form.errors.get("__all__")  # 获取全局钩子错误信息
            return render(request, "add_emp.html", {"form": form, "clear_errors": clear_errors})
