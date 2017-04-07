# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='ManholeDatabaseHistory',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('time', models.DateTimeField(verbose_name=b'date published')),
                ('relayid', models.CharField(default=b'0', max_length=30, null=True)),
                ('sensorid', models.CharField(default=b'0', max_length=30, null=True)),
                ('data', models.TextField(default=b'', null=True)),
            ],
        ),
    ]
