from django.contrib import admin
from .models import Category, Product

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ['name', 'slug']
    list_filter = ['name']
    prepopulated_fields = {'slug': ('name',)}


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ['category', 'name', 'image', 'description', 'price', 'created_at', 'updated_at', 'available']
    prepopulated_fields = {'slug': ('name',)}
    list_editable = ['price', 'available']
    list_filter = ['category', 'created_at', 'available', 'updated_at']

# Register your models here.
