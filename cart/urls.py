from . import views
from django.urls import path

app_name = 'cart'
urlpatterns = [
    path('', views.cart_detail, name = 'cart_detail'),
    path('add/<int:product_id>/<slug:slug>', views.add_cart, name = 'add-to-cart'),
    path('delete_item/<int:product_id>', views.remove_cart, name = 'remove-from-cart'),
    
    
]
