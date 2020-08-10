from django.db import models

# Create your models here.
class Product(models.Model):
    name = models.CharField(max_length=200)
    slug= models.SlugField(max_length=100)
    description = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    available = models.BooleanField(default=True)

    def __str__(self):
        return self.name

class myUser(models.Model):
    first_name = models.TextField()
    last_name = models.TextField()
    phone_number = models.TextField()
    date_joined = models.TextField()

    def __str__(self):
        return self.first_name
    