from django.urls import path
from . import views

urlpatterns = [
    path('checkout', views.checkout, name='checkout'),
    #path('home', views.index, name='index'),
    #path('contact',views.contact,name='contact')
    #path('about',views.about, name='about'),
]