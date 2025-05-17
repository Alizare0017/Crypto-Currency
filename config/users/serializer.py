from rest_framework import serializers

from .models import User
from helpers.regex_validators import validators


class UserSerializer(serializers.ModelSerializer):
    # is_common = serializers.CharField(default=User.is_common)
    # is_permium = serializers.CharField(default=User.is_planA)
    # is_permium = serializers.CharField(default=User.is_planB)

    class Meta:
        model = User
        fields = '__all__'

class _UserActionBase(serializers.Serializer):

    def create(self, validated_data):
        pass

    def update(self, instance, validated_data):
        pass

    username = serializers.CharField(validators=[validators.username])
    password = serializers.CharField(validators=[validators.password])


class RegisterUserSerializer(_UserActionBase):
    password = serializers.CharField()


class LoginSerializer(_UserActionBase):
    pass


class ChangeActiveStatusSerializer(serializers.Serializer):
    is_active = serializers.BooleanField(required=True)


class UpdateUserSerializer(serializers.Serializer):
    first_name = serializers.CharField(required=False)
    last_name = serializers.CharField(required=False)
    email = serializers.EmailField(required=False)
    phone = serializers.CharField(validators=[validators.phone], required=False)




