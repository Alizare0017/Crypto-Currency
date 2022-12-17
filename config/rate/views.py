from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.permissions import IsAdminUser
from django.utils import timezone

from users.models import User
from . import  custom_permisson_classes as cp
from rate.serializer import CurrencySerializer, GoldSerializer, CryptoSerializer
from helpers.Collector import currencyLeech, cryptoLeech
from .models import Currency, Gold, Crypto


# Create your views here.

class Manager(APIView):
    permission_classes = [IsAdminUser]
    def post(self,request,name):
        currencyleech = currencyLeech(name)
        if name == 'gold' :
            for obj in currencyleech :
                obj['updated_date'] = timezone.now()
                serializer = GoldSerializer(data=obj)
                if serializer.is_valid():
                    serializer.save()
                else:
                    return Response(status=status.HTTP_400_BAD_REQUEST, data={'errors':serializer.errors})

        if name == 'currency' :
            for obj in currencyleech :
                serializer = CurrencySerializer(data=obj)
                if serializer.is_valid():
                    serializer.save()
                else:
                    return Response(status=status.HTTP_400_BAD_REQUEST, data={'errors':serializer.errors})

        if name == 'crypto' :
            cryptoleech = cryptoLeech()
            for obj in cryptoleech :
                serializer = CryptoSerializer(data=obj)
                if serializer.is_valid():
                    serializer.save()
                else:
                    return Response(status=status.HTTP_400_BAD_REQUEST, data={'errors':serializer.errors})
        return Response(status=status.HTTP_200_OK)

    def put(self,request,name):
        if name == 'gold':
            currencyleech = currencyLeech('gold')
            for obj in currencyleech:
                serializer = GoldSerializer(data=obj)
                if serializer.is_valid():
                    Gold.objects.filter(code=obj['code']).update(price=obj['price'],rate=obj['rate'],high=obj['high'],
                                                                    low=obj['low'],updated_date=obj['updated_date'],
                                                                    requested_date=timezone.now(), time_stamp=obj['time_stamp'])
                else :
                    return Response(status=status.HTTP_400_BAD_REQUEST, data={'errors':serializer.errors})
            return Response(status=status.HTTP_200_OK)

        if name == 'currency':
            currencyleech = currencyLeech('currency')
            for obj in currencyleech:
                serializer = CurrencySerializer(data=obj)
                if serializer.is_valid():
                    Currency.objects.filter(code=obj['code']).update(price=obj['price'],rate=obj['rate'],high=obj['high'],
                                                                    low=obj['low'],updated_date=obj['updated_date'],
                                                                    requested_date=timezone.now(), time_stamp=obj['time_stamp'])
                else :
                    return Response(status=status.HTTP_400_BAD_REQUEST, data={'errors':serializer.errors})
            return Response(status=status.HTTP_200_OK)
        if name == 'crypto':
            cryptoleech = cryptoLeech()
            for obj in cryptoleech:
                serializer = CryptoSerializer(data=obj)
                if serializer.is_valid():
                    Crypto.objects.filter(rank=obj['rank']).update(price=obj['price'],name=obj['name'],rial_price=obj['rial_price'],
                                                                    marketcap=obj['marketcap'],volume=obj['volume'],
                                                                    requested_date=timezone.now(), daily_swing=obj['daily_swing'],
                                                                    weekly_swing=obj['weekly_swing'],rank=obj['rank'],code=obj['code'])
                else:
                    return Response(status=status.HTTP_400_BAD_REQUEST, data={'errors':serializer.errors})
            return Response(status=status.HTTP_200_OK)
        return Response(status=status.HTTP_400_BAD_REQUEST, data={'errors':' Something went Wrong ! '})

    def delete(self,requst,name):

        if name == 'gold':
            Gold.objects.all().delete()
            return Response(status=status.HTTP_200_OK)
        if name == 'currency':
            Currency.objects.all().delete()
            return Response(status=status.HTTP_200_OK)
        if name == 'crypto':
            Crypto.objects.all().delete()
            return Response(status=status.HTTP_200_OK)


class CurrencyView(APIView):
    
    def post(self,request):
        user = User.objects.filter(token=request.query_params.get('token'))
        if user.exists():
            currency = Currency.objects.all()
            serializer = CurrencySerializer(currency, many=True)
            return Response(status=status.HTTP_200_OK, data=serializer.data)
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

