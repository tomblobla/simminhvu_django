from django.db import models
from category.models import Category
from django.core.validators import MaxValueValidator, MinValueValidator
# Create your models here.


class Tag(models.Model):
    name = models.CharField(max_length=50, unique=True)

    def __str__(self):
        return self.name


class Product(models.Model):
    name = models.CharField(max_length=200, unique=True)
    slug = models.SlugField(max_length=200, unique=True)
    description = models.TextField(max_length=500, blank=True)
    price = models.IntegerField()
    image = models.ImageField(upload_to='photos/products')
    is_available = models.BooleanField(default=True)
    created_date = models.DateTimeField(auto_now_add=True)

    sale_off = models.IntegerField(
        default=0,
        validators=[
            MaxValueValidator(100),
            MinValueValidator(0)
        ]
    )

    category = models.ForeignKey(Category, on_delete=models.CASCADE)

    tags = models.ManyToManyField(Tag, related_name='products')

    def __str__(self):
        return self.name
    
    def get_saleprice(self):
        new_price = self.price * (100 - self.sale_off) / 100
        return new_price
