from django.contrib import admin

# Register your models here.
from core.models import Cashback, Customer, Company, Sale, SaleItem

admin.site.register(Customer)
admin.site.register(Company)
admin.site.register(Sale)
admin.site.register(SaleItem)
admin.site.register(Cashback)