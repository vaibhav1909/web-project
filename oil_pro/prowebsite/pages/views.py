from django.shortcuts import render
from django.template import loader
from django.http import HttpResponse
from customers.models import Cart
#from products.models import Contact

# Create your views here.
def checkout(request):
    #listings = Listing.objects.order_by('-list_date').filter(is_published=True)[:3]
    #template=loader.get_template('i.html')
    checkc = Cart.objects.filter(customers_id = 1)
    #print(*checkc.customer_id)
    a = 0
    for i in checkc:
        cust = (i.customers_id)
        a +=(i.product_id.product_price * i.cart_qty)
    
    context = {
        'final' :checkc,
        'cust'  :cust,
        'amt'  : a
    }
    return render(request,'checkout.html',context)
    #return HttpResponse(template.render(context,request))

