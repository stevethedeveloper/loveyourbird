from django.contrib import admin
from django.utils.html import format_html
from django.urls import reverse, path
from django.http import HttpResponse

from breeds.models import Breed, BreedImage

class BreedImageInline(admin.StackedInline):
    model = BreedImage
    extra = 1
    
class BreedAdmin(admin.ModelAdmin):
    #inlines = [BreedImageInline]
    list_display = ('common_name', 'number_of_images')

    def get_urls(self):
        urls = super().get_urls()
        custom_urls = [
            path(
                '<int:breed_id>/images/',
                self.admin_site.admin_view(self.edit_images),
                name='edit_breed_images',
            ),
        ]
        return custom_urls + urls
        
    def number_of_images(self, obj):
        return format_html(
            '<a href="{}">' + str(obj.breedimage_set.count()) + '</a>',
            reverse('admin:edit_breed_images', args=[obj.pk]),
        )
        number_of_images.short_description = 'Actions'
        number_of_images.allow_tags = True
            
    def edit_images(self, request, breed_id, *args, **kwargs):
        return HttpResponse(breed_id)

admin.site.register(Breed, BreedAdmin)
admin.site.register(BreedImage)
