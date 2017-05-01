# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('manhole_database', '0002_auto_20170501_1612'),
    ]

    operations = [
        migrations.AddField(
            model_name='sensordata',
            name='end_index',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='sensordata',
            name='index_len',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='sensordata',
            name='other_peak',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='sensordata',
            name='other_var',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='sensordata',
            name='peakvalue',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='sensordata',
            name='processed_status',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='sensordata',
            name='start_index',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='sensordata',
            name='width',
            field=models.IntegerField(default=0),
        ),
    ]
