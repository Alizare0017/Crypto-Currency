from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from rate.models import Currency
from rate.serializer import RateSerializer

# Create your views here.

class RateView(APIView):
    
    def get(self,request):
        currency = Currency.objects.all()
        serializer = RateSerializer(currency, many=True)
        print(serializer.data)
        return Response(status=status.HTTP_200_OK, data=serializer.data)
    