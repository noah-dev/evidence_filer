from django.shortcuts import render, redirect
from django.http import JsonResponse

def index(request):
    '''Render the home page, with the map'''
    return render(request, 'aaw/index.html')