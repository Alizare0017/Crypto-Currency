from rest_framework import serializers
from rate.models import Currency, Gold, Crypto, Plan


class CurrencySerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Currency
        fields = '__all__'

class GoldSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Gold
        fields = '__all__'

class CryptoSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Crypto
        fields = '__all__'

class PlanSerializer(serializers.ModelSerializer):

    class Meta:
        model = Plan
        fields = '__all__'