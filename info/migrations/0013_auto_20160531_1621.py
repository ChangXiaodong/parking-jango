# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('info', '0012_auto_20160513_1716'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='manholedata',
            name='data',
        ),
        migrations.RemoveField(
            model_name='manholedata',
            name='nodeid',
        ),
        migrations.RemoveField(
            model_name='manholedata',
            name='relayid',
        ),
        migrations.RemoveField(
            model_name='manholedatahistory',
            name='areaid',
        ),
        migrations.RemoveField(
            model_name='manholedatahistory',
            name='nodeid',
        ),
        migrations.RemoveField(
            model_name='manholedatahistory',
            name='relayid',
        ),
        migrations.AddField(
            model_name='manholedata',
            name='TMR_data',
            field=models.CharField(default=b'0', max_length=5, null=True),
        ),
        migrations.AddField(
            model_name='manholedata',
            name='address',
            field=models.BigIntegerField(default=0, null=True),
        ),
        migrations.AddField(
            model_name='manholedata',
            name='battery_data',
            field=models.CharField(default=b'0', max_length=5, null=True),
        ),
        migrations.AddField(
            model_name='manholedata',
            name='reed_data',
            field=models.CharField(default=b'0', max_length=5, null=True),
        ),
        migrations.AddField(
            model_name='manholedata',
            name='rssi_data',
            field=models.CharField(default=b'0', max_length=5, null=True),
        ),
        migrations.AddField(
            model_name='manholedata',
            name='snr_data',
            field=models.CharField(default=b'0', max_length=5, null=True),
        ),
        migrations.AddField(
            model_name='manholedata',
            name='threshold',
            field=models.CharField(default=b'0', max_length=5, null=True),
        ),
        migrations.AddField(
            model_name='manholedatahistory',
            name='address',
            field=models.BigIntegerField(default=0, null=True),
        ),
        migrations.AddField(
            model_name='manholedatahistory',
            name='data_type',
            field=models.CharField(default=b'0', max_length=3, null=True),
        ),
        migrations.AlterField(
            model_name='manholedatahistory',
            name='data',
            field=models.CharField(default=b'0', max_length=5, null=True),
        ),
    ]
