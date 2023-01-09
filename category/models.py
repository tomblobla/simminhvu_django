from django.db import models
from django.utils.html import mark_safe

# Create your models here.


class Category(models.Model):
    name = models.CharField(max_length=50, unique=True)
    slug = models.SlugField(max_length=100, unique=True)
    description = models.TextField(max_length=255, blank=True)
    image = models.ImageField(upload_to='photos/categories', blank=True)

    def img_preview(self):  # new
        return mark_safe(f'<img src = "{self.image.url}" width = "300"/>')

    def thumbnail_preview(self):  # new
        return mark_safe(f'<img src = "{self.image.url}" width = "50"/>')

    class Meta:
        verbose_name = 'category'
        verbose_name_plural = 'categories'

    def __str__(self):
        return self.name
