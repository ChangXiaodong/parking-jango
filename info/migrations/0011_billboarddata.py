# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('info', '0010_auto_20160417_1935'),
    ]

    operations = [
        migrations.CreateModel(
            name='BillBoardData',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('update_time', models.DateTimeField(default=b'2016-04-07 10:58:41')),
                ('nodeid', models.CharField(default=b'0', max_length=30, null=True)),
                ('data', models.CharField(default=b'0', max_length=30, null=True)),
            ],
        ),
    ]
