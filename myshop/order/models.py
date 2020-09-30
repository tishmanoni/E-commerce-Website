from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.urls import reverse

# Create your models here.
from django.db import models
from myonlineshop.models import Product
from django.conf import settings
from decimal import Decimal
from django.core.validators import MinValueValidator, \
                                   MaxValueValidator
from coupons.models import Coupon

from django.conf import settings
   
    
class Order(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, blank=True, null=True)
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    email = models.EmailField()
    address = models.CharField(max_length=250)
    postal_code = models.CharField(max_length=20)
    city = models.CharField(max_length=100)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    paid = models.BooleanField(default=False)
    coupon = models.ForeignKey(Coupon,
                               related_name='orders',
                               null=True,
                               blank=True,
                               on_delete=models.SET_NULL)
    discount = models.IntegerField(default=0,
                                  validators=[MinValueValidator(0),
                                      MaxValueValidator(100)])
    class Meta:
        ordering = ('-created',)
    def __str__(self):
        return f'Order {self.id}'
    def get_total_cost(self):
        total_cost = sum(item.get_cost() for item in self.items.all())
        return total_cost - total_cost * \
            (self.discount / Decimal(100))

    # def get_absolute_url(self):
    #     return reverse('orders:my_order',args=[self.id,
    #                             self.user_id,
    #                             ])
class OrderItem(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, blank=True, null=True)
    order = models.ForeignKey(Order,
                              related_name='items',
                              on_delete=models.CASCADE)
    product = models.ForeignKey(Product,
                                related_name='order_items',
                                on_delete=models.CASCADE)

    price = models.DecimalField(max_digits=10, decimal_places=2)
    quantity = models.PositiveIntegerField(default=1)

    class Meta:
        unique_together = (('user', 'order', 'product', 'price', 'quantity'),)
    def __str__(self):
        return str(self.user)
    def get_cost(self):
        return self.price * self.quantity

    def get_absolute_url(self):
        return reverse('orders:order_item',args=[self.quantity, self.order_id,
                                self.user_id,
                                ])
    
