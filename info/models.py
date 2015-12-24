from django.db import models

class ParkData(models.Model):
    time = models.DateTimeField('date published')
    relayid = models.CharField(max_length=23,null=True,default='0')
    data = models.CharField(max_length=27,null=True,default='0')
    parkid = models.CharField(max_length=5,null=True,default='0')
