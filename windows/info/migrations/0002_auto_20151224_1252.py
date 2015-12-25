# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('info', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='parkdata',
            name='data',
            field=models.CharField(default=b'0', max_length=27, null=True),
        ),
        migrations.AddField(
            model_name='parkdata',
            name='parkid',
            field=models.CharField(default=b'0', max_length=5, null=True),
        ),
        migrations.AddField(
            model_name='parkdata',
            name='relayid',
            field=models.CharField(default=b'0', max_length=23, null=True),
        ),
    ]
