from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from django.utils import timezone

from datetime import timedelta
from users.models import User
from datetime import datetime, timedelta
from rate.serializer import CurrencySerializer, GoldSerializer, CryptoSerializer
from .models import Currency, Gold, Crypto
from helpers import permissions
from update.views import CurrencyManage

# Create your views here.

class update_timer():
    def check(requested_date,self,request):
        print(requested_date, timezone.now())
        if requested_date + timedelta(minutes=1) < timezone.now():
            CurrencyManage.put(self,request)
        else :
            pass


class CurrencyView(APIView):
    
    def post(self,request):

        user = User.objects.filter(token=request.headers.get('token'))
        currency = Currency.objects.all()
        if currency.exists():
            update_timer.check(currency[0].requested_date, self,request)
 
        else :
            return Response(status=status.HTTP_304_NOT_MODIFIED, data={'error' : 'Databse is empty ! '})

        if user.exists() :
            permission=permissions.permission_validtor(user[0].month_exp,user[0].request_count,user[0].plan.daily_request_limit,user[0].day_exp_end)
            if permission=='update_day':
                user.update(day_exp_begin= timezone.now(),day_exp_end=timezone.now() +timedelta(days=1))
                serializer = CurrencySerializer(currency, many=True)
                user.update(request_count= user[0].request_count+1)
            if permission==True:
                serializer = CurrencySerializer(currency, many=True)
                user.update(request_count= user[0].request_count+1)
                return Response(status=status.HTTP_200_OK, data=serializer.data)
            elif permission=='Expierd':
                return Response(status=status.HTTP_400_BAD_REQUEST, data={'error':'Account Expierd ! '})
            else:
                return Response(status=status.HTTP_400_BAD_REQUEST, data={'error':f'Daily RequestLimit {user[0].day_exp_end}'})
        return Response(status=status.HTTP_401_UNAUTHORIZED, data={'error':'Invalid token'})


class GoldView(APIView):

    def post(self,request):
        user = User.objects.filter(token=request.headers.get('token'))
        gold = Gold.objects.all()
        if gold.exists():
            update_timer.check(gold[0].requested_date, self,request)

        else :
            return Response(status=status.HTTP_304_NOT_MODIFIED, data={'error' : 'Databse is empty ! '})
        
        if user.exists():
            permission=permissions.permission_validtor(user[0].month_exp,user[0].request_count,user[0].plan.daily_request_limit,user[0].day_exp_end)
            if permission=='update_day':
                user.update(day_exp_begin= timezone.now(),day_exp_end=timezone.now()+timedelta(days=1), request_count = 0)
                gold = Gold.objects.all()
                user.update(request_count= user[0].request_count+1)
                serializer = GoldSerializer(gold, many=True)
                return Response(status=status.HTTP_200_OK, data=serializer.data)                
            if permission==True :
                gold = Gold.objects.all()
                user.update(request_count= user[0].request_count+1)
                serializer = GoldSerializer(gold, many=True)
                return Response(status=status.HTTP_200_OK, data=serializer.data)
            elif permission=='Expierd':
                return Response(status=status.HTTP_400_BAD_REQUEST, data={'error':'Account Expierd ! '})
            else:
                return Response(status=status.HTTP_400_BAD_REQUEST, data={'error':f'Daily RequestLimit {user[0].day_exp_end}'})         
        return Response(status=status.HTTP_401_UNAUTHORIZED, data={'error':'Invalid token'})


class CryptoView(APIView):

    def post(self,request):
        user = User.objects.filter(token=request.headers.get('token'))
        crypto = Crypto.objects.all()

        if crypto.exists():
            update_timer.check(Crypto[0].requested_date, self,request)

        else :
            return Response(status=status.HTTP_304_NOT_MODIFIED, data={'error' : 'Databse is empty ! '})
        
        if user.exists():
            permission=permissions.permission_validtor(user[0].month_exp,user[0].request_count,user[0].plan.daily_request_limit,user[0].day_exp_end)
            if permission=='update_day':
                user.update(day_exp_begin= timezone.now(),day_exp_end=timezone.now()+timedelta(days=1))
                crypto = Crypto.objects.all()
                serializer = CryptoSerializer(crypto, many=True)
                user.update(request_count= user[0].request_count+1)
            if permission==True:
                crypto = Crypto.objects.all()
                serializer = CryptoSerializer(crypto, many=True)
                user.update(request_count= user[0].request_count+1)
                return Response(status=status.HTTP_200_OK, data=serializer.data)
            elif permission=='Expierd':
                return Response(status=status.HTTP_400_BAD_REQUEST, data={'error':'Account Expierd ! '})
            else:
                return Response(status=status.HTTP_400_BAD_REQUEST, data={'error':f'Daily RequestLimit {user[0].day_exp_end}'})
        return Response(status=status.HTTP_401_UNAUTHORIZED, data={'error':'Invalid token'})