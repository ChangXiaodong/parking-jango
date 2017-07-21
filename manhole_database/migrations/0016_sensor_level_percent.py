# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('manhole_database', '0015_auto_20170718_2147'),
    ]

    operations = [
        migrations.AddField(
            model_name='sensor',
            name='level_percent',
            field=models.FloatField(default=0, null=True),
        ),
    ]
