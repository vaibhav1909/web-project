from django.urls import path
from . import views

urlpatterns = [
    path('<int:product_id>',views.product,name='product'),
    path('home',views.products,name='home'),
    #path('', views.index, name='index'),
    path('contact',views.contact,name='contact'),
    path('afcontact',views.afcontact,name='afcontact'),
    #path('about',views.about, name='about'),
]