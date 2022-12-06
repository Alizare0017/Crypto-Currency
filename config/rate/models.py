from django.db import models

# Create your models here.

class Currency(models.Model):
    name = models.CharField(max_length=25)
    price = models.FloatField()
    updated_date =models.DateTimeField()
    country = models.CharField(max_length=35)
    
    def __str__(self):
        return self.name

class Test(models.Model):
    name_1 = models.CharField(max_length=5)
    name_2 = models.CharField(max_length=5)
    name_3 = models.CharField(max_length=5)
    name_4 = models.CharField(max_length=5)

    def __str__(self):
        return self.name_1