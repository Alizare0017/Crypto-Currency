from django.db import models

# Create your models here.

class Currency(models.Model):
    name = models.CharField(max_length=25)
    price = models.FloatField()
    updated_date =models.DateTimeField()
    country = models.CharField(max_length=35)
    
    def __str__(self):
        return self.name