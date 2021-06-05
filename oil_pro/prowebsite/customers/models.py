from django.db import models
from django.db.models.fields import EmailField

# Create your models here.
class Customers(models.Model):
    customers_id = models.CharField(max_length=20,primary_key=True)
    customers_fname = models.CharField(max_length=50)
    customers_lname = models.CharField(max_length=10)
    customers_address = models.CharField(max_length=10)
    customers_phone_no = models.IntegerField(default=0)
    customers_email = models.EmailField(max_length=200)
    customers_dob = models.DateField()
    #customers_photo = models
    cphoto_main=models.ImageField(upload_to='photos/%Y/%m/%d')
    customers_city = models.CharField(max_length=50)
    customers_state = models.CharField(max_length=50)
    customers_password = models.CharField(max_length=50)