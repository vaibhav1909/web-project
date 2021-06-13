from django.shortcuts import render,get_object_or_404
from django.template import loader
from django.http import HttpResponse
from .models import Contact, Product
from django.http import Http404
from django.core.mail import send_mail
from django.core.paginator import EmptyPage,PageNotAnInteger,Paginator
# Create your views here.

def afcontact(request):
    name=request.POST['name']
    email=request.POST['email']
    subject=request.POST['subject']
    text=request.POST['text']
    if name==None:
        raise Http404
    contact=Contact(contact_name=name,contact_email=email,contact_subject=subject,contact_message=text)
    contact.save()
    send_mail(
        'Contact Application Submitted',
        'Thanks '+ name  +'\n For contacting us for ' + subject + ' will respond on it soon.',
        'projecttest76@gmail.com',
        [email],
        fail_silently= False
    )
    
    #template=loader.get_template('contact.html')
    context = {
        
    }
    return render(request,'contact.html',context)
    #return HttpResponse(template.render(content,request))

def products(request):
    lproducts = Product.objects.order_by('-list_date')
    print(lproducts)
    lpaginator = Paginator(lproducts ,6)
    page = request.GET.get('page')
    lpaged_listings = lpaginator.get_page(page)
    #print(*lpaged_listings)

    products = Product.objects.order_by('list_date')
    paginator = Paginator(products , 5)
    #page = request.GET.get('page')
    paged_listings = paginator.get_page(page)
    context = {
        'llistings' : lpaged_listings,
        'listings' : paged_listings
    }
    #print(*paged_listings)
    return render(request,'i.html',context)

def product(request,product_id):
    listing = get_object_or_404(Product,product_id=product_id)
    context = {
        'listing':listing
    }
    return render(request,'product.html',context)


def contact(request):
    con ={

    }
    return render(request,'contact.html',con)