from decimal import Decimal
from django.conf import settings
from shop.models import Product

class Cart(object):
    
    def __init__(self, request):
        "initialize the cart"
        self.session = request.session
        cart = self.session.get(settings.CART_SESSION_ID)
        if not cart:
            cart = self.session[settings.CART_SESSION_ID] = {}
        self.cart = cart

    def add_cart(self, product, quantity = 1, update_quantity = False):
        "add item to cart"
        product_id = str(product.id)
        if product not in self.cart:
            self.cart[product_id] = {'quantity' :0 ,
                                    'price': str(product.price)}
        
        if update_quantity:
            self.cart[product_id]['quantity'] = [quantity]
        else:
            self.cart[product_id]['quantity'] += [quantity]
        
        self.save

    def save(self):
        "save all activities in the cart session"
        self.session.modified = True
    
    def remove(self, product):
        "Delete unwanted item in the cart"
        product_id = str(product.id)
        if product_id in self.cart:
           del self.session.cart[product_id]
           self.save()

    def __iter__(self):
       product_ids = self.cart.key()
       cart = self.cart.values()
       products = Product.objects.filter(ids__in = product_ids)
       for product in products:
           cart[str('product.id')]['product'] =product

       for item in cart.values():
            item['price'] = Decimal(item['price'])
            item['total_price'] = item['quantity'] * item['price']
            yield item       
    
    def __len__(self):
        return sum(item['quantity'] for item in self.cart.values())

    def grand_total(self):
        return sum(item['quantity'] * item['price'] for item in self.cart.values())

    def clear(self):
        del self.session[settings.CART_SESSION_ID]
        self.save()

