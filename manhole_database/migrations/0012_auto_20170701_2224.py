# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('manhole_database', '0011_autossh'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='autossh',
            name='reconnect',
        ),
        migrations.AddField(
            model_name='autossh',
            name='reconnect_flag',
            field=models.CharField(default=b'0', max_length=1),
        ),
    ]
