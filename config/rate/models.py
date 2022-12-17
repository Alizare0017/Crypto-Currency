from django.db import models
# Create your models here.

class Currency(models.Model):
    name = models.CharField(max_length=30)
    code = models.CharField(max_length=6)
    price = models.IntegerField()
    rate = models.CharField(max_length=20)
    high = models.IntegerField()
    low = models.IntegerField()
    updated_date = models.DateTimeField()
    requested_date = models.DateTimeField(auto_now_add=True)
    time_stamp = models.IntegerField(default=0)

    def __str__(self):
        return self.name

class Gold(models.Model):
    name = models.CharField(max_length=30)
    code = models.CharField(max_length=20)
    price = models.IntegerField()
    rate = models.CharField(max_length=20)
    high = models.IntegerField()
    low = models.IntegerField()
    updated_date = models.DateTimeField()
    requested_date = models.DateTimeField(auto_now_add=True)
    time_stamp = models.IntegerField(default=0)

    def __str__(self):
        return self.name

class Crypto(models.Model):
    name = models.CharField(max_length=20)
    code = models.CharField(max_length=6, default='a')
    price = models.FloatField(default=0)
    rial_price = models.FloatField(null=True)
    marketcap = models.IntegerField()
    volume = models.IntegerField()
    daily_swing = models.FloatField()
    weekly_swing = models.FloatField()
    rank = models.IntegerField()
    requested_date = models.DateTimeField(auto_now_add=True)


    def __str__(self):
        return self.name