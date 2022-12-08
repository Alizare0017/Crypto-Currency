from django.contrib import admin
from rate.models import Currency, Gold
# Register your models here.

class CurrencyAdmin(admin.ModelAdmin):
    list_display = ['id','name','code','price', 'updated_date', 'requested_date']

class GoldAdmin(admin.ModelAdmin):
    list_display = ['id','name','code','price', 'updated_date', 'requested_date']

admin.site.register(Currency, CurrencyAdmin)
admin.site.register(Gold, GoldAdmin)