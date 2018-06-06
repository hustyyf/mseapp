from django.utils import timezone
from datetime import datetime
from datetime import timedelta
from django.db import models

# Create your models here.
class Room(models.Model):
    NAME_CHOICES = (
        ('0','129'),
        ('1','136'),
        ('2','136'),
        ('3','345'),
    )
    ON_USE_CHOICES = (
        (u'y',u'usable'),
        (u'n',u'unusable'),
    )
    name = models.CharField(max_length=3,choices=NAME_CHOICES)
    status = models.CharField(max_length=2,choices=ON_USE_CHOICES)
    def __str__(self):
        return self.name

class Rent(models.Model):
    room=models.ForeignKey(Room,on_delete=models.CASCADE)
    applicant = models.CharField(max_length=10)
    apply_date=models.DateTimeField(auto_now_add=True)
    aim_date=models.DateField()
    start_time=models.TimeField()
    stop_time=models.TimeField()
    phone_num=models.CharField(max_length=11)
    apply_reason=models.CharField(max_length=50)