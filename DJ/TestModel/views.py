from django.http import HttpResponse
from django.shortcuts import render, redirect
import time
from datetime import date
from django.shortcuts import HttpResponse


def index(request):
    #print(year)  # 一个形参代表路径中一个分组的内容，按顺序匹配
    return HttpResponse('菜鸟教程')
