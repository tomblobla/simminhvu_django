from django.contrib import admin
from .models import Product, Tag, Order

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


class OrderAdmin(admin.ModelAdmin):
    list_display = (
        'SIM', 'address', 'ISP', 'Username',
    )

    def ISP(self, obj):
        return obj.product.category.name

    def SIM(self, obj):
        return obj.product.name

    def Username(self, obj):
        return obj.user.username


admin.site.register(Product, ProductAdmin)
admin.site.register(Tag, TagAdmin)
admin.site.register(Order, OrderAdmin)
