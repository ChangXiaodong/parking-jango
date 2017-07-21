# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('manhole_database', '0006_auto_20170505_1248'),
    ]

    operations = [
        migrations.CreateModel(
            name='RelayConfig',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('relayid', models.CharField(default=b'0', max_length=30, null=True)),
                ('start_time', models.DateTimeField(default=b'2016-04-07 10:58:41')),
                ('port', models.CharField(default=b'0', max_length=10)),
            ],
        ),
    ]
