import django
from django.contrib import admin
from sql.models import Customer, Product, Company

# Register your models here.
admin.site.register(Customer)
admin.site.register(Company)
admin.site.register(Product)
