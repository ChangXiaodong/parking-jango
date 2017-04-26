# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('manhole_database', '0003_auto_20170408_0121'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='configure',
            name='sensorid',
        ),
        migrations.RemoveField(
            model_name='data',
            name='sensorid',
        ),
        migrations.RemoveField(
            model_name='sensor',
            name='id',
        ),
        migrations.AlterField(
            model_name='sensor',
            name='sensorid',
            field=models.CharField(default=b'0', max_length=30, serialize=False, primary_key=True),
        ),
    ]
