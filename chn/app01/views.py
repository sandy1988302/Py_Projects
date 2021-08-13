from django.shortcuts import HttpResponse, render
from datetime import datetime
# noinspection PyUnresolvedReferences
from app01 import get_news


def start(request):
    return render(request, 'start.html')


def crawler(request):
    request.encoding = 'utf-8'
    now = datetime.now()
    localtime = now.strftime('%Y-%m-%d %H:%M:%S')
    print(localtime)
    get_news.exp_data(localtime)
    return HttpResponse('OK')
