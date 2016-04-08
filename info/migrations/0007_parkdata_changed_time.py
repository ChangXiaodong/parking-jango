# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('info', '0006_parkdata_command'),
    ]

    operations = [
        migrations.AddField(
            model_name='parkdata',
            name='changed_time',
            field=models.DateTimeField(default=b'2016-04-07 10:58:41'),
        ),
    ]
