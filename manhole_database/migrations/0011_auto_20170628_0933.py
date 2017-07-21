# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('manhole_database', '0010_auto_20170628_0910'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='sensor',
            name='quary_times',
        ),
        migrations.AddField(
            model_name='key',
            name='query_times',
            field=models.IntegerField(default=0),
        ),
    ]
