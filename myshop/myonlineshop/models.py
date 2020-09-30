from django.db import models
from django.utils import timezone
from django.urls import reverse
from django.conf import settings
from django import forms
from django.contrib.auth.models import User


# Create your models here.

class Category(models.Model):
    name = models.CharField(max_length=200, db_index = True)
    slug = models.SlugField(max_length=200, unique=True)

    class Meta:
        ordering = ('name',)
        verbose_name = 'category'
        verbose_name_plural = 'categories'
    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('myonlineshop:product_list_by_category', args=[self.slug])

COLOR_CHOICES = (
    ('Red', 'R'),
    ('Black', 'B')
)

class Product (models.Model):
    category = models.ForeignKey(Category, related_name='products', on_delete=models.CASCADE)
    name = models.CharField(max_length=100, db_index=True)
    slug = models.SlugField(max_length=200, db_index=True)
    image = models.ImageField(upload_to='products/%Y/%m/%d', blank=True, null=True)
    slider1 = models.ImageField(upload_to='products/%Y/%m/%d', blank=True, null=True)
    slider2 = models.ImageField(upload_to='products/%Y/%m/%d', blank=True, null=True)
    slider3 = models.ImageField(upload_to='products/%Y/%m/%d', blank=True, null=True)

    description = models.TextField(blank=True)
    additional_information =  models.TextField(blank=True)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    available = models.BooleanField(default=True)
    Featured= models.BooleanField(default=False)
    Premium = models.BooleanField(default=False)
    New_arrivals = models.BooleanField(default=False)
    recomended = models.BooleanField(default=False)
    new = models.BooleanField(default=False)
    best = models.BooleanField(default=False)
    header_image = models.BooleanField(default=False)
    
    sale = models.BooleanField(default=False, verbose_name='pending payments')
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    
    class Meta:
        ordering = ('name',)
        index_together = (('id', 'slug'),)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('myonlineshop:product_detail', args=[self.id, self.slug])


class Review(models.Model):
    user = models.ForeignKey(User,
                                on_delete=models.CASCADE, related_name='customer', null=True)
    product = models.ForeignKey(Product,
                             on_delete=models.CASCADE,
                             related_name='review', null=True)
    name = models.CharField(max_length=80)
    email = models.EmailField()
    body = models.TextField()
    ip =  models.CharField(max_length=20, blank=True)
    rate = models.IntegerField(default=1)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    active = models.BooleanField(default=True)
    class Meta:
        ordering = ('created',)
    def __str__(self):
        return f'Comment by {self.name} on {self.product}'

    def __str__(self):
        return f'Profile for user {self.name}'

    

    