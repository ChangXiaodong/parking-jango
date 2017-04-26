# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('manhole_database', '0007_configure_log'),
    ]

    operations = [
        migrations.CreateModel(
            name='IPTables',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('relayid', models.CharField(default=b'0', max_length=30, null=True)),
                ('net_address', models.CharField(default=b'0', max_length=6, null=True)),
                ('sensorid', models.ForeignKey(related_name='iptables_sensor_id', default=b'0', to='manhole_database.Sensor')),
            ],
        ),
    ]
