from django.shortcuts import render, redirect, get_object_or_404
from django.views.decorators.http import require_POST
from .cart import Cart
from .forms import CartForm
from shop.models import Product

@require_POST
def add_cart(request, product_id, slug):
    add_item = Cart(request)
    product = get_object_or_404(Product, id=product_id, slug = slug)
    cart_form = CartForm(request.POST)
    if cart_form.is_valid():
        cd = cart_form.cleaned_data
        add_item.add(product=product,
                 quantity=cd['quantity'],
                 update_quantity=cd['update'])
    return redirect('cart:cart_detail')



def remove_cart(request, product_id):
        remove_item = Cart(request)
        product = get_object_or_404(Product, id =product_id)
        remove_item.remove(product)
        return redirect('cart:cart_detail')

def cart_detail(request):
        cart = Cart(request)
        for item in cart:
                item['update_quantity'] = CartForm(
                        initial={'quantity': item['quantity'],
                        'update': True}
                )
        return render(request, 'cart/cart_detail.html', {'cart': cart})

