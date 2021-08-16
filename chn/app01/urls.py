from django.urls import path
# noinspection PyUnresolvedReferences
from app01 import views

urlpatterns = [
    path('start/', views.start),
    path('crawler/', views.crawler),
    path('add_emp/', views.add_emp),
    path('add_book/', views.add_book),
]
