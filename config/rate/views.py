from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from django.utils import timezone

from rate.models import Currency
from rate.serializer import CurrencySerializer, GoldSerializer, CryptoSerializer
from helpers.Collector import currencyLeech, cryptoLeech
from .models import Currency, Gold, Crypto


# Create your views here.

class RateView(APIView):
    
    def get(self,request):
        if request.data['type'] == 'currency' :
            currency = Currency.objects.all()
            serializer = CurrencySerializer(currency, many=True)
            return Response(status=status.HTTP_200_OK, data=serializer.data)
        if request.data['type'] == 'gold' :
            currency = Gold.objects.all()
            serializer = GoldSerializer(currency, many=True)
            return Response(status=status.HTTP_200_OK, data={serializer.data})           
    
    def put(self,request):
        currencyleech = currencyLeech(request.data['type'])
        for obj in currencyleech:
            if request.data['type'] == 'currency' :
                serializer = CurrencySerializer(data=obj)
                if serializer.is_valid():
                    Currency.objects.filter(code=obj['code']).update(price=obj['price'],rate=obj['rate'],high=obj['high'],
                                                                    low=obj['low'],updated_date=obj['updated_date'],
                                                                    requested_date=timezone.now(), time_stamp=obj['time_stamp'])
                else :
                    return Response(status=status.HTTP_400_BAD_REQUEST, data={'errors':serializer.errors})
            if request.data['type'] == 'gold' :
                serializer = GoldSerializer(data=obj)
                if serializer.is_valid():
                    Gold.objects.filter(code=obj['code']).update(price=obj['price'],rate=obj['rate'],high=obj['high'],
                                                                    low=obj['low'],requested_date=timezone.now()
                                                                    ,updated_date=obj['updated_date'],time_stamp=obj['time_stamp'])
                else :
                    return Response(status=status.HTTP_400_BAD_REQUEST, data={'errors':serializer.errors})
        return Response(status=status.HTTP_200_OK)

    def post(self,request):
        currencyleech = currencyLeech(request.data['type'])
        if request.data['type'] == 'gold' :
            for obj in currencyleech :
                obj['updated_date'] = timezone.now()
                serializer = GoldSerializer(data=obj)
                if serializer.is_valid():
                    serializer.save()
                else:
                    return Response(status=status.HTTP_400_BAD_REQUEST, data={'errors':serializer.errors})
        #return Response(status=status.HTTP_200_OK)
        if request.data['type'] == 'currency' :
            for obj in currencyleech :
                serializer = CurrencySerializer(data=obj)
                if serializer.is_valid():
                    serializer.save()
                else:
                    return Response(status=status.HTTP_400_BAD_REQUEST, data={'errors':serializer.errors})

        return Response(status=status.HTTP_200_OK)

class CryptoView(APIView):

    def post(self,request):
        cryptoleech = cryptoLeech()
        for obj in cryptoleech :
            serializer = CryptoSerializer(data=obj)
            if serializer.is_valid():
                serializer.save()
            else:
                return Response(status=status.HTTP_400_BAD_REQUEST, data={'errors':serializer.errors})
        return Response(status=status.HTTP_200_OK)


    def get(self,request):
        crypto = Crypto.objects.all()
        serializer = CryptoSerializer(crypto, many=True)
        return Response(status=status.HTTP_200_OK, data=serializer.data)


    def put(self,request):
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