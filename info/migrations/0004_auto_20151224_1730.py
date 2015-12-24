# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('info', '0003_parkdatahistory'),
    ]

    operations = [
        migrations.AddField(
            model_name='parkdata',
            name='nodeid',
            field=models.CharField(default=b'0', max_length=30, null=True),
        ),
        migrations.AddField(
            model_name='parkdatahistory',
            name='nodeid',
            field=models.CharField(default=b'0', max_length=30, null=True),
        ),
    ]
