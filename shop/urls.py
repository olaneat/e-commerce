from django.urls import path
from . import views


app_name = 'shop'
urlpatterns = [
    path('', views.product_list, name = 'product_list'),
    path('<slug:category_slug>', views.product_list, name = 'category-list'),
    path('<slug:slug>/<int:id>', views.product_detail, name = 'product-detail'),

]
