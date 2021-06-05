from django.db import models

# Create your models here.
class Products(models.Model):
    product_id = models.CharField(max_length=20,primary_key=True)
    product_name = models.CharField(max_length=50)
    product_type = models.CharField(max_length=10)
    product_volume = models.CharField(max_length=10)
    product_qty = models.IntegerField(default=0)
    product_price = models.IntegerField()
    product_description =  models.CharField(max_length=20)