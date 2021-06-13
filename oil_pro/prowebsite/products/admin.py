from django.contrib import admin
from .models import Contact, Product
# Register your models here.
class ProductAdmin(admin.ModelAdmin):
    list_display =('product_id','product_name','product_type','product_volume','product_qty','product_price','product_description','product_image')
    list_display_links =('product_id','product_name','product_type')
    search_fields =('product_id','product_name','product_type')
    list_per_page = 25
admin.site.register (Product , ProductAdmin)



class ContactAdmin(admin.ModelAdmin):
    list_display = ('contact_name','contact_email','contact_subject','contact_message')
    list_display_links = ('contact_email','contact_name')
    search_fields = ('contact_name','contact_email')
    list_per_page = 25
admin.site.register (Contact , ContactAdmin)