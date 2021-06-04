from django.contrib import admin
from .models import Product
from .models import Catagory
from .models import Customer

# this method is use for print name price catagory in db
class AdminProduct(admin.ModelAdmin):
    list_display = ['name','price','catagory']

class AdminCatagory(admin.ModelAdmin):
    list_display = ['name']

class AdminCustomer(admin.ModelAdmin):
    list_display = ['first_name','last_name','mobile','password','email']
# Register your models here.
admin.site.register(Product,AdminProduct)
admin.site.register(Catagory,AdminCatagory)
admin.site.register(Customer,AdminCustomer)