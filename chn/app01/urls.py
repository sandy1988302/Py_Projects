from django.urls import path, re_path
from app01 import views


urlpatterns = [
    path('start/', views.start),
    path('crawler/', views.crawler),
]
