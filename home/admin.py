from django.contrib import admin
from .models import Category,Product

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ['name','slug']

@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ['name','category','price','created','available']

