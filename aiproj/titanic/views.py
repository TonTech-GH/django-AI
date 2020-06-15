from django.shortcuts import render
from django.http import HttpResponse

def hellofunc(request):
    return HttpResponse('<h1>Hello</h1>')