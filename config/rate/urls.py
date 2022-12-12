from . import views
from django.urls import path

urlpatterns = [
    path('currency/', views.RateView.as_view(), name='currency'),
    path('gold/', views.RateView.as_view(), name='gold'),
    path('crypto/', views.CryptoView.as_view(), name='crypto'),
]
        