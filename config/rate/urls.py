from . import views
from django.urls import path

urlpatterns = [
    path('currency/', views.RateView.as_view(), name='currency'),
]
        