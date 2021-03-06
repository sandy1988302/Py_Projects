from django.conf.urls import url
from . import views, testdb, search, search2
from django.urls import re_path, path, include
from django.contrib import admin

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^hello/$', views.hello, name="h"),
    url(r'^testdb/$', testdb.testdb),
    url(r'^search-form/$', search.search_form),
    url(r'^search/$', search.search),
    url(r'^search-post/$', search2.search_post),
    url(r'^runoob/$', views.runoob),
    # path('index/', views.index),  # 普通路径
    re_path(r'^articles/([0-9]{4})/$', views.index),  # 正则路径
    re_path("^index/([0-9]{4})/$", views.index),
    re_path("^index/(?P<year>[0-9]{4})/(?P<month>[0-9]{2})/$", views.index1),
    path('tm/', include(('TestModel.urls', 'TestModel'))),
    # path("login1/", views.login, name="login"),
    # re_path(r"^login/([0-9]{2})/$", views.login, name="login"),
    re_path(r"^login/(?P<year>[0-9]{4})/$", views.login, name="login"),
    path("login1/", views.login, name="login"),
]
