from django.contrib import admin

from breeds.models import Breed, BreedImage

class BreedImageInline(admin.StackedInline):
    model = BreedImage
    extra = 1
    
class BreedAdmin(admin.ModelAdmin):
    inlines = [BreedImageInline]

admin.site.register(Breed, BreedAdmin)
#admin.site.register(BreedImage)
