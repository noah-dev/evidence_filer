from django.shortcuts import render, redirect
from django.http import JsonResponse

def index(request):
    return render(request, 'aaw/index.html')

def upload(request):
    return render(request, 'aaw/HomePage.html')

def retrival(request):
    return render(request, 'aaw/HomePage.html')

def taxonomy(request):
    return render(request, 'aaw/HomePage.html')