from django.contrib import admin

from breeds.models import Breed, BreedImage

class BreedImageInline(admin.StackedInline):
    model = BreedImage
    extra = 1
    
class BreedAdmin(admin.ModelAdmin):
    #inlines = [BreedImageInline]
    list_display = ('common_name', 'number_of_images')

    def number_of_images(self, obj):
        return obj.breedimage_set.count()

admin.site.register(Breed, BreedAdmin)
#admin.site.register(BreedImage)
