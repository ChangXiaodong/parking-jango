# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('manhole_database', '0012_auto_20170701_2224'),
    ]

    operations = [
        migrations.AddField(
            model_name='key',
            name='access_list',
            field=models.CharField(default=b'', max_length=50),
        ),
        migrations.AddField(
            model_name='sensor',
            name='ssh_reconnect',
            field=models.CharField(default=b'0', max_length=1),
        ),
    ]
