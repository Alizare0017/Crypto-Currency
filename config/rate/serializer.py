from rest_framework import serializers
from rate.models import Currency, Gold


class CurrencySerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Currency
        fields = '__all__'

class GoldSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Gold
        fields = '__all__'