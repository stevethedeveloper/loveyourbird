from django.contrib import admin

from breeds.models import Breed, BreedImage

admin.site.register(Breed)
admin.site.register(BreedImage)
