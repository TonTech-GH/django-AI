from django.urls import path
from . import views

urlpatterns = [
    path('input/', views.hellofunc, name='input'),
    path('result/', views.resultfunc, name='result'),
]
