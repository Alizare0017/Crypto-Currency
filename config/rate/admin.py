from django.contrib import admin
from rate.models import Currency
# Register your models here.

class CurrencyAdmin(admin.ModelAdmin):
    list_display = ['id','name','country','price']
    ordering = ['updated_date']
admin.site.register(Currency, CurrencyAdmin)