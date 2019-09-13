from django import forms
from .models import Order, OrderItem

class OrderForm(forms.ModelForm):
    class Meta:
        model = Order
        fields = ['first_name', 'surname', 'email', 'phone_number', 'address', 'city',]
         