from django.shortcuts import HttpResponse, render
from app02 import check_id


def input_id(request):
    return render(request, 'id.html')


def number(request):
    request.encoding = 'utf-8'
    if 'id_number' in request.GET and request.GET['id_number']:
        message = '你输入的身份证为: ' + request.GET['id_number']
        check_id.check(request.GET['id_number'])
        ctx = {'rlt': message}
    else:
        message = '你提交了空表单'
        ctx = {'rlt': message}
    return render(request, "id.html", ctx)


def admindivisions(request):
    request.encoding = 'utf-8'
    return render(request, 'id.html')
