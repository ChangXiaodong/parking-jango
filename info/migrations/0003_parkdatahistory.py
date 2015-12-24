# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('info', '0002_auto_20151224_1252'),
    ]

    operations = [
        migrations.CreateModel(
            name='ParkDataHistory',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('time', models.DateTimeField(verbose_name=b'date published')),
                ('relayid', models.CharField(default=b'0', max_length=23, null=True)),
                ('data', models.CharField(default=b'0', max_length=27, null=True)),
                ('parkid', models.CharField(default=b'0', max_length=5, null=True)),
            ],
        ),
    ]
