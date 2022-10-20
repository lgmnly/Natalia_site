from django.shortcuts import render
from django.http import HttpResponse


def index(request):
    return render(request, 'landing/index.html', )


def cv(request):
    return render(request, 'CV/cv.html', )


def shop(request):
    return render(request, 'shop/shop.html', )