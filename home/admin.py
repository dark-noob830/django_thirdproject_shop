from django.contrib import admin
from .models import Category, Product


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ['name', 'slug','sub_category']


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    raw_id_fields = ('category',)
    list_display = ['name', 'price', 'created', 'available','get_categories']

    def get_categories(self, obj):
        return ", ".join([category.name for category in obj.category.all()])