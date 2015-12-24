from django.db import models

class ParkData(models.Model):
    time = models.DateTimeField('date published')
    relayid = models.CharField(max_length=30,null=True,default='0')
    nodeid = models.CharField(max_length=30,null=True,default='0')
    data = models.CharField(max_length=30,null=True,default='0')
    parkid = models.CharField(max_length=5,null=True,default='0')

class ParkDataHistory(models.Model):
    time = models.DateTimeField('date published')
    relayid = models.CharField(max_length=30,null=True,default='0')
    nodeid = models.CharField(max_length=30,null=True,default='0')
    data = models.CharField(max_length=30,null=True,default='0')
    parkid = models.CharField(max_length=5,null=True,default='0')
