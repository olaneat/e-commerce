from django.contrib import admin
from .models import Order, OrderItem
# Register your models here.

class OrderItemInline(admin.TabularInline):
    model = OrderItem
    raw_id_fields = ['product_list']

@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    list_display = ['first_name', 'surname', 'address', 'email', 'paid']
    list_filter = ['paid', 'created']
    inlines = [OrderItemInline]
