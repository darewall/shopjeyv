from django.contrib import admin
from .models import Category, ClothingItem



@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ['name', 'slug']
    list_filter = ['name']
    
    prepopulated_fields = {'slug': ('name',)}


@admin.register(ClothingItem)
class ClothingItemAdmin(admin.ModelAdmin):
    list_display = ['category', 'name', 'image', 'description',  'price', 'discount', 'created_at', 'updated_at', 'available']
    prepopulated_fields = {'slug': ('name',)}
    list_editable = ['price', 'available', 'discount']
    list_filter = ['category', 'created_at', 'available', 'updated_at']
    ordering = ['-created_at']
# Register your models here.
