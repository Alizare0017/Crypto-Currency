from . import views
from django.urls import path

urlpatterns = [
    path('currency/', views.CurrencyManage.as_view(), name='currency-magnage'),
    path('gold/<int:pk>', views.GoldManage.as_view(), name='gold-magnage'),
    path('crypto/<int:pk>', views.CryptoManage.as_view(), name='crypto-magnage'),
]