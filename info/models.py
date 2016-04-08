from django.db import models

class ParkData(models.Model):
    time = models.DateTimeField('date published')
    changed_time = models.DateTimeField(default='2016-04-07 10:58:41')
    relayid = models.CharField(max_length=30,null=True,default='0')
    nodeid = models.CharField(max_length=30,null=True,default='0')
    data = models.CharField(max_length=30,null=True,default='0')
    parkid = models.CharField(max_length=5,null=True,default='0')
    command = models.CharField(max_length=5,null=True,default='0')

class ParkDataHistory(models.Model):
    time = models.DateTimeField('date published')
    relayid = models.CharField(max_length=30,null=True,default='0')
    nodeid = models.CharField(max_length=30,null=True,default='0')
    data = models.CharField(max_length=30,null=True,default='0')
    parkid = models.CharField(max_length=5,null=True,default='0')

class ManholeData(models.Model):
    update_time = models.DateTimeField('date published')
    changed_time = models.DateTimeField(default='2016-04-07 10:58:41')
    relayid = models.CharField(max_length=30,null=True,default='0')
    areaid = models.CharField(max_length=5,null=True,default='0')
    nodeid = models.CharField(max_length=30,null=True,default='0')
    command = models.CharField(max_length=5,null=True,default='0')
    data = models.CharField(max_length=30,null=True,default='0')
    last_disable_time = models.DateTimeField(default='2016-04-07 10:58:41')
    administrator = models.CharField(max_length=20,null=True,default='xiaoxiami')
    remarks = models.CharField(max_length=100,null=True,default='')
    

class ManholeDataHistory(models.Model):
    update_time = models.DateTimeField('date published')
    last_disable_time = models.DateTimeField(default='2016-04-07 10:58:41')
    relayid = models.CharField(max_length=30,null=True,default='0')
    nodeid = models.CharField(max_length=30,null=True,default='0')
    data = models.CharField(max_length=30,null=True,default='0')
    areaid = models.CharField(max_length=5,null=True,default='0')
    administrator = models.CharField(max_length=20,null=True,default='xiaoxiami')
