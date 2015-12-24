# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('info', '0004_auto_20151224_1730'),
    ]

    operations = [
        migrations.AlterField(
            model_name='parkdata',
            name='data',
            field=models.CharField(default=b'0', max_length=30, null=True),
        ),
        migrations.AlterField(
            model_name='parkdata',
            name='relayid',
            field=models.CharField(default=b'0', max_length=30, null=True),
        ),
        migrations.AlterField(
            model_name='parkdatahistory',
            name='data',
            field=models.CharField(default=b'0', max_length=30, null=True),
        ),
        migrations.AlterField(
            model_name='parkdatahistory',
            name='relayid',
            field=models.CharField(default=b'0', max_length=30, null=True),
        ),
    ]
