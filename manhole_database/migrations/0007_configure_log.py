# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('manhole_database', '0006_merge'),
    ]

    operations = [
        migrations.CreateModel(
            name='Configure_Log',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('target_relayid', models.CharField(default=b'0', max_length=30, null=True)),
                ('target_sensorid', models.CharField(default=b'0', max_length=30, null=True)),
                ('time', models.DateTimeField(verbose_name=b'date published')),
                ('finish_time', models.DateTimeField(verbose_name=b'date published')),
                ('finished', models.BooleanField(default=False)),
            ],
        ),
    ]
