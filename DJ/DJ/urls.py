from django.urls import include, path
from . import views

urlpatterns = [
    path('polls/', include('polls.urls')),
    path('hello/', views.hello),
]
