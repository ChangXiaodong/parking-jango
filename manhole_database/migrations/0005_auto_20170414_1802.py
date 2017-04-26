# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('manhole_database', '0004_auto_20170414_1759'),
    ]

    operations = [
        migrations.AddField(
            model_name='configure',
            name='sensorid',
            field=models.ForeignKey(related_name='configure_sensor_id', default=b'0', to='manhole_database.Sensor'),
        ),
        migrations.AddField(
            model_name='data',
            name='sensorid',
            field=models.ForeignKey(related_name='data_sensor_id', default=b'0', to='manhole_database.Sensor'),
        ),
    ]
