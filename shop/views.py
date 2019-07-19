from django.shortcuts import render
from .models import Product, Category
from django.shortcuts import get_object_or_404, reverse
from django.http import HttpResponseRedirect
# Create your views here.

def product_list(request, category_slug = None):
    category = None
    categories = Category.objects.all()
    product = Product.objects.filter(available = True)
    if category_slug:
        category = get_object_or_404(Category, slug = category_slug)
        product = product.filter(category = category)
    return render(request, 'shop/index.html', {
        'categories': categories,
        'product': product,
        'category': category})

def product_detail(request, id, slug):
    product = get_object_or_404(Product, 
                                slug =slug,
                                id = id,
                                available = True )
    return render(request, 'shop/product-detail.html',
                                 {'product': product})                


