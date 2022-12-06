from rest_framework import serializers
from rate.models import Currency


class CurrencySerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Currency
        fields = '__all__'