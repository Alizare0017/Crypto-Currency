from django.urls import path
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView

from . import views

urlpatterns = [
    path("", views.ListRegisterUserView.as_view(), name="users"),
    path("login/", views.LoginView.as_view(), name="login"),
    path("logout/", views.LogoutView.as_view(), name="logout"),
    path('subscribe/', views.SubscribeView.as_view(), name = 'subscribe'),
    path('token/', TokenObtainPairView.as_view(), name = 'token'),
    path('refresh/token/', TokenRefreshView.as_view(), name = 'token_refresh'),
]