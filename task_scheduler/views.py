from django.http import HttpResponse
from django.shortcuts import render


def index(request):
    return render(request, 'home.html')

def completed(request):
    return render(request, 'home.html')

def urgent(request):
    return render(request, 'home.html')

def overdue(request):
    return render(request, 'home.html')

def login(request):
    return render(request, 'login.html')