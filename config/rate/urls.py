from . import views
from django.urls import path

urlpatterns = [
    path('currency/', views.RateView.as_view(), name='currency'),
    path('test/', views.TestView.as_view()),
]
        