# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('info', '0008_manholedata_manholedatahistory'),
    ]

    operations = [
        migrations.AlterField(
            model_name='parkdatahistory',
            name='data',
            field=models.CharField(default=b'0', max_length=900, null=True),
        ),
    ]
