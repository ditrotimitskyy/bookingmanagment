from django.contrib import admin
from .models import Cabin, LivingTime, CabinNum, Visitor
# Register your models here.

admin.site.register(Cabin)
admin.site.register(LivingTime)
admin.site.register(CabinNum)
admin.site.register(Visitor)