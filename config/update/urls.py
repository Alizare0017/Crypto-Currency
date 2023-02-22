from . import views
from django.urls import path

urlpatterns = [
    path('currency/', views.CurrencyManage.as_view(), name='currency-magnage'),
    path('gold/', views.GoldManage.as_view(), name='gold-magnage'),
    path('crypto/', views.CryptoManage.as_view(), name='crypto-magnage'),
    path('plan/', views.PlanMange.as_view(), name='plan-magnage'),
]