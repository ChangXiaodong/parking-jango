# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('manhole_database', '0012_auto_20170705_1008'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='autossh',
            name='access_list',
        ),
        migrations.AddField(
            model_name='key',
            name='access_list',
            field=models.CharField(default=b'', max_length=50),
        ),
    ]
