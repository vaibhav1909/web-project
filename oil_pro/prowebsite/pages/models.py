from datetime import date, datetime
from django.db import models
from products.models import Product
from customers.models import Customer,Cart
from django.db.models.fields import EmailField


# Create your models here.
class Sale(models.Model):
    sale = models.ForeignKey(Cart,on_delete=models.DO_NOTHING)
    price = models.ImageField()
    sdate = models.DateTimeField(default=datetime.now,blank=True)
