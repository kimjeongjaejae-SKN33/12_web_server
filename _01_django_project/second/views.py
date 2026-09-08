
from django.shortcuts import render


def index(request):
    return render(request, 'second/index.html')


def hello(request):
    return render(request, 'second/hello.html')