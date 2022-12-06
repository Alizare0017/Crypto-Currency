from django.db import models
import datetime
# Create your models here.

class Currency(models.Model):
    name = models.CharField(max_length=30)
    code = models.CharField(max_length=3)
    price = models.IntegerField()
    rate = models.CharField(max_length=20)
    high = models.IntegerField()
    low = models.IntegerField()
    updated_date = models.TimeField()
    requested_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name

class Test(models.Model):
    name_1 = models.CharField(max_length=5)
    name_2 = models.CharField(max_length=5)
    name_3 = models.CharField(max_length=5)
    name_4 = models.CharField(max_length=5)

    def __str__(self):
        return self.name_1