from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.permissions import IsAdminUser
from django.utils import timezone

from datetime import timedelta
from users.models import User
from . import  custom_permisson_classes as cp
from rate.serializer import CurrencySerializer, GoldSerializer, CryptoSerializer
from .models import Currency, Gold, Crypto, Plan


# Create your views here.

class CurrencyView(APIView):
    
    def post(self,request):
        user = User.objects.filter(token=request.query_params.get('token'))
        if user.exists():
            if user.month_exp > timezone.datetime.now():
                plan = Plan.objects.filter(pk=user.plan_id)
                if user.request_count <= plan.daily_request_limit :
                    currency = Currency.objects.all()
                    serializer = CurrencySerializer(currency, many=True)
                    user.update(request_count=+1)
                    return Response(status=status.HTTP_200_OK, data=serializer.data)
                elif user.day_exp < timezone.datetime.now():
                    user.update(day_exp=timezone.datetime.now() + timedelta(days=1))
                    currency = Currency.objects.all()
                    serializer = CurrencySerializer(currency, many=True)
                    return Response(status=status.HTTP_200_OK, data=serializer.data)
                else:
                    return Response(status=status.HTTP_400_BAD_REQUEST, data={'error':'daily request limit !'})
            return Response(status=status.HTTP_400_BAD_REQUEST, data={'error':'token expired !'})
        return Response(status=status.HTTP_401_UNAUTHORIZED, data={'error':'Invalid token'})


class GoldView(APIView):

    def post(self,request):
        user = User.objects.filter(token=request.query_params.get('token'))
        if user.exists():
            gold = Gold.objects.all()
            serializer = GoldSerializer(gold, many=True)
            return Response(status=status.HTTP_200_OK, data=serializer.data)           
        return Response(status=status.HTTP_401_UNAUTHORIZED, data={'error':'Invalid token'})


class CryptoView(APIView):

    def post(self,request):
        user = User.objects.filter(token=request.query_params.get('token'))
        if user.exists():       
            crypto = Crypto.objects.all()
            serializer = CryptoSerializer(crypto, many=True)
            return Response(status=status.HTTP_200_OK, data=serializer.data)
        return Response(status=status.HTTP_401_UNAUTHORIZED, data={'error':'Invalid token'})