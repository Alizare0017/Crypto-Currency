from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from users.models import User
from users.serializer import UserSerializer
from . import  custom_permisson_classes as cp
from rate.serializer import CurrencySerializer, GoldSerializer, CryptoSerializer
from .models import Currency, Gold, Crypto, Plan
from helpers import permissions

# Create your views here.


class CurrencyView(APIView):
    
    def post(self,request):
        user = User.objects.filter(token=request.query_params.get('token'))            
        if user.exists():
            if permissions.permission_validtor(user[0].month_exp,user[0].request_count,user[0].plan.daily_request_limit,user[0])==True:
                currency = Currency.objects.all()
                serializer = CurrencySerializer(currency, many=True)
                user.update(request_count= user[0].request_count+1)
                return Response(status=status.HTTP_200_OK, data=serializer.data)
            else:
                return Response(status=status.HTTP_400_BAD_REQUEST, data={'error':'denied!'})
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