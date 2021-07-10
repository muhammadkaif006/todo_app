import datetime

from django.db import models

# Create your models here.

class tasks(models.Model):
    heading = models.CharField(max_length=100)
    description = models.CharField(max_length=250)
    date = models.DateField(default=datetime.date.today)
    time = models.TimeField(default=datetime.time)
