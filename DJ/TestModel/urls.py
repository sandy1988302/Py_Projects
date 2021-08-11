from django.urls import path, re_path
from TestModel import views  # 从自己的 app 目录引入 viewsimport views

urlpatterns = [
    # path('login', views.index),
    path("login/", views.login, name="login")
]
