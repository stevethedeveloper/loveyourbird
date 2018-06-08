from django.shortcuts import render
from django.http import HttpResponse
from django.views import generic

from .models import Breed, BreedImage

def index(request):
    """Home page for breeds"""
    
    #Get all breed featured images
    images = BreedImage.objects.select_related('breed').filter(featured=1).order_by('breed__common_name')
    
    context = {'images': images}
    
    return render(request, 'breeds/index.html', context)

def detail(request, breed_id):
    """Home page for breeds"""
    
    #Get all breed featured images
    breed = Breed.objects.get(pk=breed_id)
    
    context = {'breed': breed}
    
    return render(request, 'breeds/detail.html', context)

