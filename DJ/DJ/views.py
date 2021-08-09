from django.http import HttpResponse
from django.shortcuts import render
import time
from datetime import date


def hello(request):
    return HttpResponse("Hello world ! ")


def runoob(request):
    name = "菜鸟教程"
    return render(request, "runoob.html", {"name": name})
