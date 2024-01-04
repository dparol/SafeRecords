from django.contrib import admin
from .models import Account,BusinessManager,BusinessEmployee,QrCoeData

# Register your models here.


admin.site.register(Account)
admin.site.register(BusinessManager)
admin.site.register(BusinessEmployee)
admin.site.register(QrCoeData)