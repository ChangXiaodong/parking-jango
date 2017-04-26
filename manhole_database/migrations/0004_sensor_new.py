# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('manhole_database', '0003_auto_20170408_0121'),
    ]

    operations = [
        migrations.AddField(
            model_name='sensor',
            name='new',
            field=models.BooleanField(default=True),
        ),
    ]
