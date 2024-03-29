from rest_framework.views import APIView
from rest_framework.permissions import IsAdminUser
from django.utils import timezone
from rest_framework import status


from rest_framework.response import Response
from helpers.Collector import currencyLeech, cryptoLeech
from update.serializer import GoldSerializer, CurrencySerializer, CryptoSerializer
from rate.models import Gold, Currency, Crypto
# Create your views here.

class GoldManage(APIView):
    permission_classes = [IsAdminUser]
    def post(self,request):
        currencyleech = currencyLeech('gold')
        for obj in currencyleech :
            obj['updated_date'] = timezone.now()
            serializer = GoldSerializer(data=obj)
            if serializer.is_valid():
                serializer.save()
            else:
                return Response(status=status.HTTP_400_BAD_REQUEST, data={'errors':serializer.errors})
        return Response(status=status.HTTP_200_OK)    


    def put(self,request):
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

    def delete(self,requst,name):

        Gold.objects.all().delete()
        return Response(status=status.HTTP_200_OK)

class CurrencyManage(APIView):

    def post(self,request):
        currencyleech = currencyLeech('currency')
        for obj in currencyleech :
                serializer = CurrencySerializer(data=obj)
                if serializer.is_valid():
                    serializer.save()
                else:
                    return Response(status=status.HTTP_400_BAD_REQUEST, data={'errors':serializer.errors})
        return Response(status=status.HTTP_200_OK)

    def put(self,request):
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

    def delete(self,request):    
        Currency.objects.all().delete()
        return Response(status=status.HTTP_200_OK)


class CryptoManage(APIView):

    def post(self,request):
        cryptoleech = cryptoLeech()
        for obj in cryptoleech :
            serializer = CryptoSerializer(data=obj)
            if serializer.is_valid():
                serializer.save()
            else:
                return Response(status=status.HTTP_400_BAD_REQUEST, data={'errors':serializer.errors})
        return Response(status=status.HTTP_200_OK)

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

    def delete(self,request):
        Crypto.objects.all().delete()
        return Response(status=status.HTTP_200_OK)