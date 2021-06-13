from django.contrib import admin
from .models import Customer,Cart
from products.models import Product
# Register your models here.
class CustomerAdmin(admin.ModelAdmin):
    list_display = ('customer_id','customer_fname','customer_lname','customer_address','customer_phone_no','customer_email','customer_dob','customer_photo','customer_city','customer_state','customer_password') 
    list_display_links = ('customer_email','customer_id')
    search_fields = ('customer_email','customer_id')
    list_per_page = 25
admin.site.register (Customer , CustomerAdmin)

class CartAdmin(admin.ModelAdmin):
    list_display = ('customers_id','product_id','cart_qty')
    list_display_links = ('customers_id','product_id','cart_qty')
    search_fields = ('customers_id','product_id','cart_qty')
    list_per_page = 25
admin.site.register (Cart , CartAdmin)