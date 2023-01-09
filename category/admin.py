from django.contrib import admin
from .models import Category
# Register your models here.


class CategoryAdmin(admin.ModelAdmin):  # new
    readonly_fields = ['img_preview']
    prepopulated_fields = {
        'slug': ('name',)
    }

    list_display = ('name', 'description', 'thumbnail_preview')


admin.site.register(Category, CategoryAdmin)  # new
