from django.db import models

class Breed(models.Model):
    """Common breeds of pet birds"""
    common_name = models.CharField(max_length=255, blank=False)
    binomial_name = models.CharField(max_length=255, blank=True, null=True)
    summary = models.TextField(blank=True, null=True)
    pet_information = models.TextField(blank=True, null=True)
    description = models.TextField(blank=True, null=True)
    description_source = models.CharField(max_length=255, blank=True, null=True)
    food = models.TextField(blank=True, null=True)
    size = models.CharField(max_length=50, blank=True, null=True)
    sound = models.TextField(blank=True, null=True)
    talking = models.TextField(blank=True, null=True)
    social = models.TextField(blank=True, null=True)
    breeding = models.TextField(blank=True, null=True)
    country_of_origin = models.CharField(max_length=255, blank=True, null=True)
    date_added = models.DateTimeField(auto_now_add=True, null=True)
    
    def __str__(self):
        """Return the common name"""
        return self.common_name
