from django.db import models
from datetime import datetime

# Create your models here.
class Product(models.Model):
    product_id = models.CharField(max_length=20,primary_key=True)
    product_name = models.CharField(max_length=50)
    product_type = models.CharField(max_length=10)
    product_volume = models.CharField(max_length=10)
    product_qty = models.IntegerField(default=0)
    product_price = models.IntegerField()
    product_description =  models.CharField(max_length=500)
    product_image = models.ImageField(upload_to='photos/%Y/%m/%d')
    is_published=models.BooleanField(default=True)
    list_date=models.DateTimeField(default=datetime.now,blank=True)
    def __str__(self):
        return self.product_id

class Contact(models.Model):
    contact_name = models.CharField(max_length=50)
    contact_email = models.EmailField()
    contact_subject = models.CharField(max_length=50)
    contact_message = models.CharField(max_length=400)