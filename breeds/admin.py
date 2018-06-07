from django.contrib import admin
from django.forms.models import BaseInlineFormSet
from django.core.exceptions import ValidationError

from breeds.models import Breed, BreedImage

class ImageInlineFormSet(BaseInlineFormSet):
    def clean(self):
        super(ImageInlineFormSet, self).clean()
        total = 0
        for form in self.forms:
            if not form.is_valid():
                return  # other errors exist
            if form.cleaned_data and not form.cleaned_data.get('DELETE'):
                if form.cleaned_data['featured'] == 1:
                    total += 1
        if total != 1:
            raise ValidationError('A breed should have one featured image.  Please select one image as the default.')

class BreedImageInline(admin.StackedInline):
    model = BreedImage
    formset = ImageInlineFormSet
    extra = 3
    fields = ['title', 'image_name', 'image_thumb', 'featured']
    readonly_fields = ['image_thumb']

class BreedAdmin(admin.ModelAdmin):
    list_display = ('common_name', 'number_of_images')

    inlines = [BreedImageInline]

    def number_of_images(self, obj):
        return str(obj.breedimage_set.count())
        number_of_images.short_description = '# of images'

admin.site.register(Breed, BreedAdmin)
admin.site.register(BreedImage)
