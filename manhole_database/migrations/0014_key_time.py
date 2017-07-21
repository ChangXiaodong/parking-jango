# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('manhole_database', '0013_auto_20170705_1010'),
    ]

    operations = [
        migrations.AddField(
            model_name='key',
            name='time',
            field=models.DateTimeField(default=b'2016-04-07 10:58:41'),
        ),
    ]
