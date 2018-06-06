from django.shortcuts import render
from django.http import HttpResponse

from .models import Breed, BreedImage

def index(request):
    """Home page for breeds"""
    
    #Get all breed featured images
    images = BreedImage.objects.all()
    
    context = {'images': images}
    
    return render(request, 'breeds/index.html', context)
