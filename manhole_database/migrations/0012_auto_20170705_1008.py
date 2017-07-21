# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('manhole_database', '0011_auto_20170628_0933'),
    ]

    operations = [
        migrations.CreateModel(
            name='AutoSSH',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('reconnect_flag', models.CharField(default=b'0', max_length=1)),
                ('name', models.CharField(default=b'xiaoxiami', max_length=20)),
                ('access_list', models.CharField(default=b'', max_length=50)),
            ],
        ),
        migrations.AddField(
            model_name='sensor',
            name='ssh_reconnect',
            field=models.CharField(default=b'0', max_length=1),
        ),
    ]
