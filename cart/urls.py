from django.urls import path
from . import views

app_name = 'cart'


urlpatterns = [
    path('', views.cart_detail, name='cart-detail'),
    path('add/<int:item_id>/', views.add_cart, name='add-cart'),
    path('remove/<int:item_id>/', views.remove_cart, name='remove-cart'),
    path('update/<int:item_id>/', views.UpdatedView.as_view(), name='update-cart')
]
