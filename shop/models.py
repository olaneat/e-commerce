from django.db import models
from django.shortcuts import reverse


class Category(models.Model):
    name = models.CharField(max_length = 150, db_index = True)
    slug = models.SlugField(max_length= 150, db_index= True)

    class Meta:
        ordering = ('name',)
        verbose_name = 'Category'
        verbose_name_plural = 'Categories'
        
    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse("shop:category-list", args=[self.slug])
    
    
class Product(models.Model):
    name = models.CharField(max_length = 150, db_index = True)
    slug = models.SlugField(max_length= 150, db_index= True)
    description = models.TextField()
    available = models.BooleanField(default= True)
    price = models.DecimalField(max_digits= 10, decimal_places=2)
    category = models.ForeignKey(Category, on_delete = 'models.CASCADE')
    stock = models.IntegerField()
    image = models.ImageField(upload_to = 'media/img')
    created = models.DateField()

    class Meta:
        ordering = ('created',)
        index_together = (('id', 'slug'))
        verbose_name = 'Product'
        verbose_name_plural = 'Products'

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse("shop:product-detail", args=[self.slug, self.id])


    
        



# Create your models here.
