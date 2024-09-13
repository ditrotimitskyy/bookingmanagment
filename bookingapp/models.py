from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class Visitor(models.Model):
    Visitor = models.OneToOneField(User, on_delete=models.CASCADE)
    with_kid = models.BooleanField()
    ...

    class Meta:
        db_table = 'Visitors'
        verbose_name = "Booked cabin with Visitors"

class Cabin(models.Model):
    cabin_number = models.CharField(max_length=50)
    cabin_type = models.CharField(max_length=50)

    class Meta():
        ordering = ['cabin_number', 'cabin_type']



class LivingTime(models.Model):
    cabin = models.ForeignKey(Cabin, on_delete=models.SET_DEFAULT, default="unknown plane")
    #maybe add_cabin model
    start_day = models.CharField(max_length=100)
    end_day =  models.CharField(max_length=100)
                 
class CabinNum(models.Model):
    liv_time = models.ForeignKey(LivingTime, on_delete=models.CASCADE)
    visitor = models.OneToOneField(Visitor, on_delete=models.CASCADE)
    
    class Meta:
        verbose_name = "Free cabin"
        verbose_name_plural = "Free cabins"
