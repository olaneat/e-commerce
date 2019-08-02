from django.shortcuts import render
from .models import Order, OrderItem
from cart.cart import Cart
from .forms import OrderForm

# Create your views here.

def make_order(request):
    shop_cart = Cart(request)
    if request.method == 'POST':
        order_form = OrderForm(request)
        if order_form.is_valid():
            order = order_form.save()
            for item in shop_cart:
                OrderItem.objects.create(order = order,
                                        product = item['product'],
                                        price = item['price'],
                                        quantity = item['quantity'])
        shop_cart.clear()
        return render(request, 'order/order_made.html', {'order': order})
    else:
        order_form = OrderForm()
        return render(request, 'order/make_order.html', {'shop_cart': shop_cart, 'order_form': order_form})

