from django.shortcuts import render
from django.http import HttpResponse

def index(request):
    """Home page for breeds"""
    return render(request, 'breeds/index.html')
