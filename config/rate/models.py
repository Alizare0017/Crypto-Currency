from django.db import models
# Create your models here.

class Currency(models.Model):
    name = models.CharField(max_length=30)
    code = models.CharField(max_length=3)
    price = models.IntegerField()
    rate = models.CharField(max_length=20)
    high = models.IntegerField()
    low = models.IntegerField()
    updated_date = models.DateTimeField()
    requested_date = models.DateTimeField(auto_now_add=True)

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

    def __str__(self):
        return self.name