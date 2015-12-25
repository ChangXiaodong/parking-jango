# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('info', '0005_auto_20151224_1742'),
    ]

    operations = [
        migrations.AddField(
            model_name='parkdata',
            name='command',
            field=models.CharField(default=b'0', max_length=5, null=True),
        ),
    ]
