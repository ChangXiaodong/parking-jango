# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('info', '0009_auto_20160416_0028'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='parkdatahistory',
            name='nodeid',
        ),
        migrations.AddField(
            model_name='parkdatahistory',
            name='record',
            field=models.TextField(default=b'', null=True),
        ),
        migrations.AlterField(
            model_name='parkdatahistory',
            name='data',
            field=models.TextField(default=b'', null=True),
        ),
    ]
