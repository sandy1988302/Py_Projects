from django.urls import path
# noinspection PyUnresolvedReferences
from app02 import views

urlpatterns = [
    path('input/', views.input_id, name='input'),
    path('number/', views.number),
    path('admindivisions/', views.admindivisions),
    path('get/', views.get_id, name="get_id"),
    path('get_city/', views.get_city, name="get_city"),
    path('get_county/', views.get_county, name="get_county"),
]
