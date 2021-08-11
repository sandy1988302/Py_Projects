from django.http import HttpResponse
from django.shortcuts import render, redirect
import time
from datetime import date
from django.shortcuts import HttpResponse
from django.views.decorators.csrf import csrf_exempt
from django.urls import reverse


def index(request):
    # print(year)  # 一个形参代表路径中一个分组的内容，按顺序匹配
    return HttpResponse('菜鸟教程')


@csrf_exempt
def login(request):
    if request.method == "GET":
        return HttpResponse('使用的是GET')
    else:
        username = request.POST.get('username')
        pwd = request.POST.get('pwd')
        if username == "u" and pwd == "p":
            return HttpResponse('username和pwd都是 菜鸟教程')
        else:
            return redirect(reverse('TestModel:login'))
