from django.shortcuts import render, get_object_or_404, redirect
from main.models import ClothingItem
from .cart import Cart
from django.views import View


def cart_detail(request):
    cart = Cart(request)
    return render(request, 'cart/cart_detail.html', {'cart': cart})


def add_cart(request, item_id):
    cart = Cart(request)
    clothing_item = ClothingItem.objects.get(id=item_id)
    cart.add(clothing_item)
    return redirect('cart:cart-detail')


def remove_cart(request, item_id):
    cart = Cart(request)
    clothing_item = get_object_or_404(ClothingItem, id=item_id)
    cart.remove(clothing_item)
    return redirect('cart:cart-detail')


class UpdatedView(View):
    def post(self, request, item_id):
        cart = Cart(request)
        quantity = request.POST.get('quantity', '1')
        try:
            quantity = int(quantity)
            if quantity < 1:
                quantity = 1    
        except ValueError:
            quantity = 1
        clothing_item = get_object_or_404(ClothingItem, id=item_id)
        if quantity > 0:
            cart.add(clothing_item, quantity)
        else:
            cart.remove(clothing_item)
        return redirect('cart:cart-detail')




# Create your views here.
