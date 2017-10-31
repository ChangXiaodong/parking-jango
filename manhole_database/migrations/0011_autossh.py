# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('manhole_database', '0010_key'),
    ]

    operations = [
        migrations.CreateModel(
            name='AutoSSH',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('reconnect', models.DateTimeField(default=b'2016-04-07 10:58:41')),
                ('name', models.CharField(default=b'xiaoxiami', max_length=20)),
            ],
        ),
    ]
