from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from django.utils import timezone

from rate.models import Currency
from rate.serializer import CurrencySerializer , TeseSerializer
from helpers.Collector import currencyLeech
from .models import Currency


# Create your views here.

class RateView(APIView):
    
    def get(self,request):
        currency = Currency.objects.all()
        serializer = CurrencySerializer(currency, many=True)
        return Response(status=status.HTTP_200_OK, data=serializer.data)
    
    def put(self,request):
        currencyleech = currencyLeech()
        for obj in currencyleech:
            serializer = CurrencySerializer(data=obj)
            if serializer.is_valid():
                Currency.objects.filter(code=obj['code']).update(price=obj['price'],rate=obj['rate'],high=obj['high'],
                                                                 low=obj['low'],updated_date=obj['updated_date'],
                                                                 requested_date=timezone.now())
            else :
                return Response(status=status.HTTP_400_BAD_REQUEST, data={'errors':serializer.errors})
        return Response(status=status.HTTP_200_OK)


class TestView(APIView):

    def post(self,request):
        ordinary_dict = {}
        print(type(request), request.data)
        serializer = TeseSerializer(data=ordinary_dict)
        if serializer.is_valid():
            serializer.save()
            return Response(status=status.HTTP_200_OK)
        else :
            return Response(status=status.HTTP_400_BAD_REQUEST, data={'errors':serializer.errors}) 