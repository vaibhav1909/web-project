from django.db.models.aggregates import Count
from django.db.models.query import QuerySet
from django.shortcuts import render
from .models import Customer,Cart
from products.models import Product 
# Create your views here.


def cart(request):
    citem = Cart.objects.filter(customers_id = 1)
    a = 0
    for i in citem:
        a +=(i.product_id.product_price * i.cart_qty)
    items ={
        'citems' : citem,
        'pitems' : a
    }
    return render(request,'cart.html',items)

