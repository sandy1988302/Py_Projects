from django.http import HttpResponse
from django.shortcuts import render, redirect
import time
from datetime import date
from django.shortcuts import HttpResponse


def hello(request):
    return HttpResponse("Hello world ! ")


def runoob(request):
    return redirect("/index/")


def index(request, year):
    print(year)  # 一个形参代表路径中一个分组的内容，按顺序匹配
    return HttpResponse('菜鸟教程')


def index1(request, year, month):
    print(year, month)  # 一个形参代表路径中一个分组的内容，按关键字对应匹配
    return HttpResponse('菜鸟教程')
