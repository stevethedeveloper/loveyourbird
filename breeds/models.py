from django.db import models
from django.db.models import Count
from ckeditor.fields import RichTextField
from ckeditor_uploader.fields import RichTextUploadingField

class Breed(models.Model):
    """Common breeds of pet birds"""
    common_name = models.CharField(max_length=255, blank=False)
    binomial_name = models.CharField(max_length=255, blank=True, null=True)
    summary = RichTextUploadingField(blank=True, null=True)
    pet_information = RichTextUploadingField(blank=True, null=True)
    description = RichTextUploadingField(blank=True, null=True)
    description_source = models.CharField(max_length=255, blank=True, null=True)
    food = RichTextUploadingField(blank=True, null=True)
    size = models.CharField(max_length=50, blank=True, null=True)
    sound = RichTextUploadingField(blank=True, null=True)
    talking = RichTextUploadingField(blank=True, null=True)
    social = RichTextUploadingField(blank=True, null=True)
    breeding = RichTextUploadingField(blank=True, null=True)
    country_of_origin = models.CharField(max_length=255, blank=True, null=True)
    date_added = models.DateTimeField(auto_now_add=True, null=True)
    
    def __str__(self):
        """Return the common name"""
        return self.common_name
        
class BreedImage(models.Model):
    """Images for bird breeds"""
    breed = models.ForeignKey(Breed, on_delete=models.CASCADE)
    title = models.CharField(max_length=255, blank=True, null=True)
    image_name = models.ImageField(upload_to='breed_images', null=True)
    date_added = models.DateTimeField(auto_now_add=True, null=True)

    def __str__(self):
        """Return the image name"""
        return self.title
    
