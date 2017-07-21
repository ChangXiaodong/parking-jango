# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('manhole_database', '0007_relayconfig'),
    ]

    operations = [
        migrations.RenameField(
            model_name='relayconfig',
            old_name='port',
            new_name='local_port',
        ),
        migrations.AddField(
            model_name='relayconfig',
            name='remote_port',
            field=models.CharField(default=b'0', max_length=10),
        ),
    ]
