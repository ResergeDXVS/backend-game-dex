from django.contrib import admin

# Register your models here.
from .models import Accounts, Address, CreditCard

admin.site.register(Accounts)
admin.site.register(Address)
admin.site.register(CreditCard)