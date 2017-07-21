# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('manhole_database', '0005_auto_20170502_1029'),
    ]

    operations = [
        migrations.AlterField(
            model_name='sensor',
            name='battery',
            field=models.CharField(default=b'0', max_length=10, null=True),
        ),
    ]
