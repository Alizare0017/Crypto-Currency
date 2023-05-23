from rest_framework.views import APIView
from rest_framework.generics import GenericAPIView
from rest_framework.permissions import IsAuthenticated, IsAdminUser
from rest_framework import status
from rest_framework.response import Response
from rest_framework.authtoken.models import Token
from helpers.general import response, unauthorized
from django.shortcuts import get_object_or_404
from django.utils import timezone
from django.db.utils import IntegrityError
from django.contrib.auth import login
from users.models import User, Plan
from . import serializer as cs
from datetime import timedelta

# Create your views here.

class ListRegisterUserView(APIView):
    permission_classes = [IsAdminUser]
    def post(self, request):
        serializer = cs.RegisterUserSerializer(data=request.data)
        if serializer.is_valid():
            try:
                user = User.objects.create_user(**serializer.data)
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


class SubscribeView(APIView):
    permission_classes = [IsAdminUser]
    def put(self,request):
        user = User.objects.filter(username=request.data['username'])
        if user.exists():
            plan = Plan.objects.filter(pk=request.data['plan'])
            user.update(plan=request.data['plan'],month_exp=timezone.now() + timedelta(days=30),
                        day_exp_begin=timezone.now(), day_exp_end=timezone.now()+timedelta(days=1))
            return Response(status=status.HTTP_200_OK, data={'Info' : 'User updated'})
        return Response(status=status.HTTP_400_BAD_REQUEST, data={'error' : 'User not found ! '})
    
    def post(self,request):
        user = get_object_or_404(User , username = request.data['username'])
        serializer = cs.UserSerializer(user)
        return Response(status=status.HTTP_200_OK, data=serializer.data)
        # return Response(status=status.HTTP_401_UNAUTHORIZED, data={'errors':'User not found ! '})
