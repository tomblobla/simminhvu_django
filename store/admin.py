from django.contrib import admin
from .models import Product, Tag

# Register your models here.


class ProductAdmin(admin.ModelAdmin):
    list_display = (
        'name',
        'description',
        'price',
        'category',
        'created_date',
        'is_available'
    )

    search_fields = ['name', 'price', 'created_date',
                     'is_available', 'category__name']

    list_filter = ['category__name', 'tags__name']

    prepopulated_fields = {
        'slug': ('name', )
    }


class TagAdmin(admin.ModelAdmin):
    list_display = (
        'name',
    )


admin.site.register(Product, ProductAdmin)
admin.site.register(Tag, TagAdmin)
