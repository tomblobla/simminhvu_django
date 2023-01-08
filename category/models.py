from django.db import models

# Create your models here.
class Category(models.Model):
    name = models.CharField(max_length=50, unique=True)
    slug = models.CharField(max_length=100, unique=True)
    description = models.CharField(max_length=255, blank=True)
    image = models.ImageField(upload_to='photos/categories', blank=True)
    
    def __str__(self):
        return self.name