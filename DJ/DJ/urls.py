from django.urls import include, path, re_path
from . import views

urlpatterns = [
    path('polls/', include('polls.urls')),
    # path('hello/', views.hello),
    re_path(r'^hello$', views.hello),
    path('runoob/', views.runoob),
]
