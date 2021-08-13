from django.shortcuts import HttpResponse, render
from app02 import check_id, get_ad


def input_id(request):
    return render(request, 'id.html')


def number(request):
    request.encoding = 'utf-8'
    print(request.POST['id_number'])
    if request.POST['id_number']:
        message = check_id.check(request.POST['id_number'])
    else:
        message = '你提交了空表单'
    ctx = {'rlt': message}
    return render(request, "id.html", ctx)


def admindivisions(request):
    request.encoding = 'utf-8'
    get_ad.exp_db()
    return render(request, 'id.html')
