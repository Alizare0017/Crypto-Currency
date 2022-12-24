from django.contrib import admin
from rate.models import Currency, Gold, Crypto, Plan
# Register your models here.

class CurrencyAdmin(admin.ModelAdmin):
    list_display = ['id','name','code','price', 'updated_date', 'requested_date']

class GoldAdmin(admin.ModelAdmin):
    list_display = ['id','name','code','price', 'updated_date', 'requested_date']

class CryptoAdmin(admin.ModelAdmin):
    list_display = ['id','name','rial_price','price', 'requested_date']

class PlanAdmin(admin.ModelAdmin):
    list_display = ['id','name']


admin.site.register(Currency, CurrencyAdmin)
admin.site.register(Gold, GoldAdmin)
admin.site.register(Crypto, CryptoAdmin)
admin.site.register(Plan, PlanAdmin)
