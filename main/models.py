from django.db import models



class Category(models.Model):
    name = models.CharField(max_length=75, unique=True)
    slug = models.SlugField(max_length=75, unique=True)

    def __str__(self):
        return self.name
    

class Product(models.Model):
    category = models.ForeignKey(Category, related_name='category', on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    slug = models.SlugField(max_length=100)
    image = models.ImageField(upload_to='product/%Y/%m/%d', blank=True)
    description = models.TextField()
    available = models.BooleanField(default=True)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name









# Create your models here.
