from django.db import models
from django.contrib.auth.models import AbstractUser
from django.core.validators import RegexValidator
from helpers.generator import Token_Generator
from django.conf import settings
from rate.models import Plan


# class SecUser(models.Model):
#     password = models.CharField(max_length=64, null=True)


class User(AbstractUser):
    COMMON = "COMMON"
    PREMIUM = "PREMIUM"
    role_choices = (
        (COMMON, "common"),
        (PREMIUM, "premium"),
    )
    phone = models.CharField(
        max_length=13, validators=[RegexValidator(regex=settings.PHONE_REGEX)], null=True, blank=True
    )
    # pointless = models.ForeignKey(SecUser, on_delete=models.CASCADE)
    role = models.CharField(max_length=8, choices=role_choices, null=True, blank=True, default=COMMON)
    username = models.CharField(max_length=50,unique=True)
    is_phone_activated = models.BooleanField(default=False)
    is_email_activated = models.BooleanField(default=False)
    token = models.CharField(max_length=40,default=Token_Generator,unique=True)
    plan = models.ForeignKey(Plan, on_delete=models.CASCADE,db_constraint=False, null=True)
    request_count = models.IntegerField(default=0)
    month_exp = models.DateTimeField(null=True)
    day_exp_begin = models.DateTimeField(null=True)
    day_exp_end = models.DateTimeField(null=True)


    # @property
    # def is_planA(self):
    #     return self.plan == self.planA

    # @property
    # def is_planB(self):
    #     return self.plan == self.planB
    
    # @property
    # def is_common(self):
    #     return self.plan == self.COMMON

    @property
    def full_name(self):
        return self.first_name + self.last_name
    

