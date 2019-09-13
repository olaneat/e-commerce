from decimal import Decimal
from django.conf import settings
from shop.models import Product, Category


class Cart(object):

    def __init__(self, request):
        self.session = request.session 
        cart = self.session(settings.CART_SESSION_ID)
        if not cart:
            cart = self.session(settings.CART_SESSION_ID) = {}
        self.cart = cart

    def add_cart(self, quantityy = 1, update_cart = False):
        product_id = str(Product.id)
        
