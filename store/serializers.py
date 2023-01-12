from rest_framework.serializers import ModelSerializer
from rest_framework import serializers
from .models import Category, Product, Tag


class CategorySerializer(ModelSerializer):
    class Meta:
        model = Category
        fields = ["id", "image", "name",
                  "description", "products", 'slug']


class ProductSerializer(ModelSerializer):
    category_id = serializers.IntegerField(source='category.id')
    category_name = serializers.CharField(source='category.name')
    category_slug = serializers.CharField(source='category.slug')
    category_image = serializers.ImageField(source='category.image')

    class Meta:
        model = Product
        fields = ["id", "name", "description",
                  "price", 'get_saleprice', "sale_off", "tags", 'slug',
                  "category_name", "category_id", "category_image", "category_slug"]


class TagSerializer(ModelSerializer):
    class Meta:
        model = Tag
        fields = ["id", "name", 'products']
