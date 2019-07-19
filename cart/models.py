from django.db import models
from django.shortcuts import reverse
from shop.models import Product, Category

# Create your models here.
class cart(models.Model):
    quantity = models.CharField(max_length = 10)
    