from django.db import models
from datetime import datetime

# Create your models here.
class Users(models.Model):
    username = models.CharField(max_length=100)
    email = models.CharField(max_length=50)
    location = models.CharField(max_length=50)

class Product(models.Model):
    product_title = models.CharField(max_length=200)
    product_base_price = models.DecimalField(max_digits=12, decimal_places=2)
    product_description = models.TextField()
    product_date_added = models.DateTimeField(default=datetime.now, blank=True)
    sold = models.BooleanField(default=False)

