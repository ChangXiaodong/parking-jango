# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('manhole_database', '0003_auto_20170501_1615'),
    ]

    operations = [
        migrations.DeleteModel(
            name='SensorData',
        ),
    ]
