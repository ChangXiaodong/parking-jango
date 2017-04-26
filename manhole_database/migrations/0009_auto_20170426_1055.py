# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('manhole_database', '0008_iptables'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='sensor',
            name='manual',
        ),
        migrations.AddField(
            model_name='configure',
            name='get_valid_data_WIDTH',
            field=models.IntegerField(default=0, null=True),
        ),
        migrations.AddField(
            model_name='configure',
            name='listened_data_COUNT',
            field=models.IntegerField(default=0, null=True),
        ),
        migrations.AddField(
            model_name='configure',
            name='listened_data_SLOP',
            field=models.IntegerField(default=0, null=True),
        ),
        migrations.AddField(
            model_name='configure',
            name='listened_data_STABLECNT',
            field=models.IntegerField(default=0, null=True),
        ),
        migrations.AddField(
            model_name='configure',
            name='open_angle_cnt',
            field=models.IntegerField(default=0, null=True),
        ),
        migrations.AddField(
            model_name='configure',
            name='open_angle_threshold',
            field=models.IntegerField(default=0, null=True),
        ),
        migrations.AddField(
            model_name='configure',
            name='split_data_MEAN_WIDTH_1',
            field=models.IntegerField(default=0, null=True),
        ),
        migrations.AddField(
            model_name='configure',
            name='split_data_MEAN_WIDTH_2',
            field=models.IntegerField(default=0, null=True),
        ),
        migrations.AddField(
            model_name='configure',
            name='split_data_VAR_LEN',
            field=models.IntegerField(default=0, null=True),
        ),
        migrations.AddField(
            model_name='configure',
            name='split_data_WIDTH',
            field=models.IntegerField(default=0, null=True),
        ),
        migrations.AddField(
            model_name='configure',
            name='update_middlevalue_cnt',
            field=models.IntegerField(default=0, null=True),
        ),
        migrations.AlterField(
            model_name='sensor',
            name='period',
            field=models.CharField(default=b'0', max_length=10, null=True),
        ),
    ]
