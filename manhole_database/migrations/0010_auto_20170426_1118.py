# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('manhole_database', '0009_auto_20170426_1055'),
    ]

    operations = [
        migrations.RenameField(
            model_name='sensor',
            old_name='manhole_installed_time',
            new_name='manhole_used_time',
        ),
    ]
