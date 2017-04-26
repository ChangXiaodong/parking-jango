# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('manhole_database', '0002_auto_20170408_0120'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='ManholeDatabaseSensorConfigure',
            new_name='Configure',
        ),
        migrations.RenameModel(
            old_name='ManholeDatabaseData',
            new_name='Data',
        ),
        migrations.RenameModel(
            old_name='ManholeDatabaseSensor',
            new_name='Sensor',
        ),
    ]
