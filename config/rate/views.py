from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from rate.models import Currency
from rate.serializer import CurrencySerializer

# Create your views here.

class RateView(APIView):
    
    def get(self,request):
        currency = Currency.objects.all()
        serializer = CurrencySerializer(currency, many=True)
        print(serializer.data)
        return Response(status=status.HTTP_200_OK, data=serializer.data)
    
    def post(self,request):
        print(type(request), request.data)
        serializer = CurrencySerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(status=status.HTTP_200_OK)
        else :
            return Response(status=status.HTTP_400_BAD_REQUEST, data={'errors':serializer.errors})