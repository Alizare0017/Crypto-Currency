from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from django.utils import timezone

from rate.models import Currency
from rate.serializer import CurrencySerializer, GoldSerializer
from helpers.Collector import currencyLeech
from .models import Currency, Gold


# Create your views here.

class RateView(APIView):
    
    def get(self,request):
        if request.data['type'] == 'currecy' :
            currency = Currency.objects.all()
            serializer = CurrencySerializer(currency, many=True)
            return Response(status=status.HTTP_200_OK, data=serializer.data)
        if request.data['type'] == 'gold' :
            currency = Gold.objects.all()
            serializer = GoldSerializer(currency, many=True)
            return Response(status=status.HTTP_200_OK, data=serializer.data)           
    
    def put(self,request):
        currencyleech = currencyLeech(request.data['type'])
        for obj in currencyleech:
            if request.data['type'] == 'currency' :
                serializer = CurrencySerializer(data=obj)
                if serializer.is_valid():
                    Currency.objects.filter(code=obj['code']).update(price=obj['price'],rate=obj['rate'],high=obj['high'],
                                                                    low=obj['low'],updated_date=obj['updated_date'],
                                                                    requested_date=timezone.now())
                else :
                    return Response(status=status.HTTP_400_BAD_REQUEST, data={'errors':serializer.errors})
            if request.data['type'] == 'gold' :
                obj['code'] = 'asd'
                serializer = GoldSerializer(data=obj)
                if serializer.is_valid():
                    serializer.save()
                    # Gold.objects.filter(code=obj['code']).update(price=obj['price'],rate=obj['rate'],high=obj['high'],
                    #                                                 low=obj['low'],updated_date=obj['updated_date'],
                    #                                                 requested_date=timezone.now())
                else :
                    return Response(status=status.HTTP_400_BAD_REQUEST, data={'errors':serializer.errors})
            return Response(status=status.HTTP_200_OK)
        return Response(status=status.HTTP_400_BAD_REQUEST, data={'errors':serializer.errors})

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