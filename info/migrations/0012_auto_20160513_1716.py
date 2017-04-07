# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('info', '0011_billboarddata'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='billboarddata',
            name='data',
        ),
        migrations.AddField(
            model_name='billboarddata',
            name='x',
            field=models.CharField(default=b'0', max_length=30, null=True),
        ),
        migrations.AddField(
            model_name='billboarddata',
            name='y',
            field=models.CharField(default=b'0', max_length=30, null=True),
        ),
    ]
