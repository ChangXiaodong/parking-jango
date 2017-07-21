# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('manhole_database', '0008_auto_20170511_2127'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='sensor',
            name='new',
        ),
        migrations.AddField(
            model_name='configure',
            name='angle_wake',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='preconfigure',
            name='angle_wake',
            field=models.IntegerField(default=0),
        ),
    ]
