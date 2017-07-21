# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('manhole_database', '0009_auto_20170513_1758'),
    ]

    operations = [
        migrations.CreateModel(
            name='Key',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('src', models.CharField(default=b'0', max_length=30)),
                ('key', models.CharField(default=b'0', max_length=40)),
            ],
        ),
        migrations.AddField(
            model_name='sensor',
            name='quary_times',
            field=models.IntegerField(default=0),
        ),
    ]
