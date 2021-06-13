from django.db import models
from products.models import Product
from django.db.models.fields import EmailField

# Create your models here.
class Customer(models.Model):
    customer_id = models.CharField(max_length=20,primary_key=True)
    customer_fname = models.CharField(max_length=50)
    customer_lname = models.CharField(max_length=10)
    customer_address = models.CharField(max_length=10)
    customer_pincode = models.ImageField()
    customer_phone_no = models.IntegerField(default=0)
    customer_email = models.EmailField(max_length=200)
    customer_dob = models.DateField()
    #customer_photo = models
    customer_photo=models.ImageField(upload_to='photos/%Y/%m/%d')
    customer_city = models.CharField(max_length=50)
    customer_state = models.CharField(max_length=50)
    customer_password = models.CharField(max_length=50)
    def __str__(self):
        return self.customer_id

class Cart(models.Model):
    customers_id = models.ForeignKey(Customer,on_delete=models.DO_NOTHING)
    product_id = models.ForeignKey(Product,on_delete=models.DO_NOTHING)
    cart_qty = models.IntegerField()
    def __str__(self):
        return str(self.customers_id)