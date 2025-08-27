from django.shortcuts import render, get_object_or_404
from .models import Category, ClothingItem



def product_list(request, category_slug=None):
    
    category = None
    categories = Category.objects.all()
    products = ClothingItem.objects.filter(available=True)
    if category_slug:
        category = get_object_or_404(Category, slug=category_slug)
        products = ClothingItem.objects.filter(category=category, available=True)

    return render(request, 'main/product/list_product.html', {'category': category, 'categories': categories, 'products': products})


def product_detail(request, slug):
    product = get_object_or_404(ClothingItem, slug=slug)
    contex_data = {
        'product': product
    }

    return render(request, 'main/product/detail.html', contex_data)