from django.db import models

class Breed(models.Model):
    """Common breeds of pet birds"""
    common_name = models.CharField(max_length=255, blank=False)
    binomial_name = models.CharField(max_length=255, blank=True)
    description = models.TextField(blank=True)
    description_source = models.CharField(max_length=255, blank=True)
    food = models.TextField(blank=True)
    size = models.CharField(max_length=50, blank=True)
    sound = models.TextField(blank=True)
    talking = models.TextField(blank=True)
    social = models.TextField(blank=True)
    country_of_origin = models.CharField(max_length=255, blank=True)
    date_added = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        """Return the common name"""
        return self.common_name
