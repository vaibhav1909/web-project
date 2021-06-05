from django.shortcuts import render
from django.template import loader
from django.http import HttpResponse

# Create your views here.
def index(request):
    #listings = Listing.objects.order_by('-list_date').filter(is_published=True)[:3]
    #template=loader.get_template('i.html')
    context = {
        
    }
    return render(request,'index.html',context)
    #return HttpResponse(template.render(context,request))