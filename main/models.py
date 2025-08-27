from django.db import models
from django.urls import reverse


class Category(models.Model):
    name = models.CharField(max_length=75, unique=True)
    slug = models.SlugField(max_length=75, unique=True)

    def __str__(self):
        return self.name
    
    class Meta:
        ordering = ('name',)
        verbose_name='Category'
        verbose_name_plural = 'Categories'
    def get_absolute_url(self):
        return reverse("main:product_list_by_category", kwargs={"category_slug": self.slug})
    

class ClothingItem(models.Model):
    category = models.ForeignKey(Category, related_name='clothing_items', on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    slug = models.SlugField(max_length=100)
   
    image = models.ImageField(upload_to='product/%Y/%m/%d', blank=True)
    description = models.TextField()
    available = models.BooleanField(default=True)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    discount = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name
    
    def get_price_with_discount(self):
        if self.discount > 0:
            return round(self.price * (1 - (self.discount / 100)), 2)
        return round(self.price, 2)
    
    def get_absolute_url(self):
        return reverse("main:product_detail", kwargs={"slug": self.slug})
    







# Create your models here.
