from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.generics import GenericAPIView
from rest_framework.permissions import IsAuthenticated
from rest_framework import status
from rest_framework.authtoken.models import Token
from helpers.general import response, unauthorized, logout
from django.shortcuts import get_object_or_404
from django.db.utils import IntegrityError
from django.contrib.auth import login
from users.models import User
from . import serializer as cs, custom_permisson_classes as cp

# Create your views here.

class ListRegisterUserView(APIView):

    def post(self, request):
        serializer = cs.RegisterUserSerializer(data=request.data)

        if serializer.is_valid():
            try:
                user = User.objects.create_user(**serializer.data, role=User.COMMON)
            except IntegrityError as e:
                return response(status.HTTP_400_BAD_REQUEST, errors=str(e))
            return response(status.HTTP_201_CREATED, instance=user, serializer=cs.UserSerializer)
        return response(status.HTTP_400_BAD_REQUEST, errors=serializer.errors)



class LoginView(APIView):

    def post(self, request, format=None):

        serializer = cs.LoginSerializer(data=request.data)
        if not serializer.is_valid():
            return response(errors=serializer.errors, status_code=status.HTTP_400_BAD_REQUEST)
        data = serializer.data

        user = get_object_or_404(User, username=data.get("username"))
        if not user.is_active:
            return unauthorized()

        if not user.check_password(data.get("password")):
            return response(
                detail="provided username and password dont match",
                errors="wrong_credentials", status_code=status.HTTP_401_UNAUTHORIZED
            )
        login(request, user)
        token = Token.objects.get_or_create(user=user)
        return response(
            detail=f"{user.username} logged in successfully",
            status_code=status.HTTP_200_OK, token=token[0].key
        )


class LogoutView(GenericAPIView):
    permission_classes = [IsAuthenticated]
    def post(self, request, format=None):
        request.user.auth_token.delete()
        return response(detail="Successfully logged out", status_code=status.HTTP_200_OK)
