from django.db import models
from shop.models import Product
# Create your models here.

class Order(models.Model):
    first_name = models.CharField(max_length = 150)
    surname =  models.CharField(max_length = 150)
    email =  models.EmailField(blank = True)
    phone_number = models.CharField(max_length = 11)
    address = models.CharField(max_length= 500)
    city = models.CharField(max_length = 150)
    paid = models.BooleanField(default= False)
    created = models.DateTimeField()
    

    class Meta:
        ordering = ('-created',)
    
    def __str__(self):
        return 'order {}'.format(self.id)
    
    def get_total_cost(self):
        return sum(item.get_cost() for item in self.items.all())


class OrderItem(models.Model):
    item_order = models.ForeignKey(Order, on_delete=models.CASCADE, related_name='items')
    product_list = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='order_items')
    price = models.DecimalField(max_digits= 9, decimal_places=2)
    quantity = models.PositiveIntegerField(default = 1)

    def __str__(self):
        return '{}'.format(self.id)
    
    def get_cost(self):
        return self.price * self.quantity
