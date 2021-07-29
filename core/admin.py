from django.contrib import admin

# Register your models here.
from core.models import Cashback, Client, Company, Sale, SaleItem

admin.site.register(Client)
admin.site.register(Company)
admin.site.register(Sale)
admin.site.register(SaleItem)
admin.site.register(Cashback)