from django.contrib import admin
from .models import Account,BusinessManager,BusinessEmployee,Barcode_Data

# Register your models here.


admin.site.register(Account)
admin.site.register(BusinessManager)
admin.site.register(BusinessEmployee)
admin.site.register(Barcode_Data)