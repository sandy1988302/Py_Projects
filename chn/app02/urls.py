from django.urls import path
# noinspection PyUnresolvedReferences
from app02 import views

urlpatterns = [
    path('input/', views.input_id),
    path('number/', views.number),
    path('admindivisions/', views.admindivisions),
]
