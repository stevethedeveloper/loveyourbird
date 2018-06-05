from django.contrib import admin
from django.utils.html import format_html
from django.urls import reverse, path
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, redirect

from breeds.models import Breed, BreedImage

class BreedAdmin(admin.ModelAdmin):
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
        breed_record = Breed.objects.get(pk=breed_id)
        image_records = BreedImage.objects.filter(breed_id=breed_id)
        return render(request,
                        'admin/breed_image_list.html',
                        context={'title':'Images for ' + breed_record.common_name, 'breed_id':breed_id, 'image_records':image_records})
        #return HttpResponse(breed_id)

class BreedImageAdmin(admin.ModelAdmin):
    list_display = ('title', 'image_tag')

    deleted_fk = None

    def delete_view(self, request, object_id, extra_context=None):
        self.deleted_fk = BreedImage.objects.get(id=object_id).breed_id
        return super(BreedImageAdmin, self).delete_view(request, object_id, extra_context)

    def response_delete(self, request, obj_display, obj_id):
        return redirect('/admin/breeds/breed/' + str(self.deleted_fk) + '/images/')
        
    #fields = ['image_tag', 'image_name', 'title', 'breed_id']
    #readonly_fields = ['image_tag']

admin.site.register(Breed, BreedAdmin)
admin.site.register(BreedImage, BreedImageAdmin)
