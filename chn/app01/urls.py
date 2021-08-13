from django.urls import path
# noinspection PyUnresolvedReferences
from app01 import views


urlpatterns = [
    path('start/', views.start),
    path('crawler/', views.crawler),
]
