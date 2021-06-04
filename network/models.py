from django.utils import timezone
from datetime import datetime
from django.db import models

# Create your models here.

class Acceleration(models.Model):
    Ax = models.FloatField(default=0)
    Bx = models.FloatField(default=0)
    count = models.IntegerField(default=0)
    sleeptime = models.DateTimeField(null=True,default=timezone.now())

    class Meta:
        db_table = "Acceleration"


class Sound(models.Model):
    sound = models.FloatField(default=0)
    count = models.IntegerField(default=0)
    sleeptime = models.DateTimeField(null=True,default=datetime.now())
    class Meta:
        db_table = "Sound"