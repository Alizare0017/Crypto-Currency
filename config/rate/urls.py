from . import views
from django.urls import path

urlpatterns = [
    path('currency/', views.CurrencyView.as_view(), name='currency'),
    path('gold/', views.GoldView.as_view(), name='gold'),
    path('crypto/', views.CryptoView.as_view(), name='crypto'),
    path('test/',views.CeleryTest.as_view(),name='test')
]