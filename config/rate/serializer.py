from rest_framework import serializers
from rate.models import Currency, Test


class CurrencySerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Currency
        fields = '__all__'

class TeseSerializer(serializers.ModelSerializer):

    class Meta:

        model = Test
        fields = '__all__'