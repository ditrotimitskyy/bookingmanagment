from django.db import models
from django.contrib.auth.models import User
from datetime import time
# Create your models here.

class Visitor(models.Model):
    Visitor = models.OneToOneField(User, on_delete=models.CASCADE)
    with_family = models.BooleanField()
    ...

    class Meta:
        db_table = 'Visitors'
        verbose_name = "cabin Visitor"

class Cabin(models.Model):
    cabin_number = models.CharField(max_length=50)
    cabin_type = models.CharField(max_length=50)

    class Meta():
        ordering = ['cabin_number', 'cabin_type']



class LivingTime(models.Model): #booking
    cabin = models.ForeignKey(Cabin, on_delete=models.SET_DEFAULT, default="unknown plane")
    #maybe add_cabin model
    start_day = models.CharField(max_length=100)
    end_day =  models.CharField(max_length=100)
                 
class CabinNum(models.Model):
    liv_time = models.ForeignKey(LivingTime, on_delete=models.CASCADE)
    visitor = models.ForeignKey(Visitor, on_delete=models.CASCADE)

    
    class Meta:
        verbose_name = "booked cabin"
        verbose_name_plural = "booked cabins"