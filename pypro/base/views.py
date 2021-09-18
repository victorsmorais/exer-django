from django.http import HttpResponse # noqa
from django.shortcuts import render


def home(request):
    return render(request, 'base/home.html')
