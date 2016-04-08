# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('info', '0007_parkdata_changed_time'),
    ]

    operations = [
        migrations.CreateModel(
            name='ManholeData',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('update_time', models.DateTimeField(verbose_name=b'date published')),
                ('changed_time', models.DateTimeField(default=b'2016-04-07 10:58:41')),
                ('relayid', models.CharField(default=b'0', max_length=30, null=True)),
                ('areaid', models.CharField(default=b'0', max_length=5, null=True)),
                ('nodeid', models.CharField(default=b'0', max_length=30, null=True)),
                ('command', models.CharField(default=b'0', max_length=5, null=True)),
                ('data', models.CharField(default=b'0', max_length=30, null=True)),
                ('last_disable_time', models.DateTimeField(default=b'2016-04-07 10:58:41')),
                ('administrator', models.CharField(default=b'xiaoxiami', max_length=20, null=True)),
                ('remarks', models.CharField(default=b'', max_length=100, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='ManholeDataHistory',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('update_time', models.DateTimeField(verbose_name=b'date published')),
                ('last_disable_time', models.DateTimeField(default=b'2016-04-07 10:58:41')),
                ('relayid', models.CharField(default=b'0', max_length=30, null=True)),
                ('nodeid', models.CharField(default=b'0', max_length=30, null=True)),
                ('data', models.CharField(default=b'0', max_length=30, null=True)),
                ('areaid', models.CharField(default=b'0', max_length=5, null=True)),
                ('administrator', models.CharField(default=b'xiaoxiami', max_length=20, null=True)),
            ],
        ),
    ]
