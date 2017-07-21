# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('manhole_database', '0004_delete_sensordata'),
    ]

    operations = [
        migrations.CreateModel(
            name='PreConfigure',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('relayid', models.CharField(default=b'0', max_length=30, null=True)),
                ('sensorid', models.CharField(default=b'0', max_length=10)),
                ('update_time', models.DateTimeField(default=django.utils.timezone.now)),
                ('acc_scale', models.IntegerField(default=0)),
                ('acc_fchoice', models.IntegerField(default=0)),
                ('acc_dlpf', models.IntegerField(default=5)),
                ('gyo_scale', models.IntegerField(default=2)),
                ('gyo_fchoice', models.IntegerField(default=1)),
                ('gyo_dlpf', models.IntegerField(default=6)),
                ('split_data_VAR_LEN', models.IntegerField(default=3)),
                ('split_data_MEAN_WIDTH_1', models.IntegerField(default=20)),
                ('split_data_MEAN_WIDTH_2', models.IntegerField(default=10)),
                ('get_valid_data_WIDTH', models.IntegerField(default=2)),
                ('split_data_WIDTH', models.IntegerField(default=20)),
                ('update_middlevalue_cnt', models.IntegerField(default=5000)),
                ('listened_data_STABLECNT', models.IntegerField(default=300)),
                ('listened_data_SLOP', models.IntegerField(default=400)),
                ('listened_data_COUNT', models.IntegerField(default=700)),
                ('open_angle_threshold', models.IntegerField(default=30)),
                ('open_angle_cnt', models.IntegerField(default=500)),
            ],
        ),
        migrations.DeleteModel(
            name='Configure_Log',
        ),
        migrations.AlterField(
            model_name='configure',
            name='acc_dlpf',
            field=models.IntegerField(default=5),
        ),
        migrations.AlterField(
            model_name='configure',
            name='acc_fchoice',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='configure',
            name='acc_scale',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='configure',
            name='get_valid_data_WIDTH',
            field=models.IntegerField(default=2),
        ),
        migrations.AlterField(
            model_name='configure',
            name='gyo_dlpf',
            field=models.IntegerField(default=6),
        ),
        migrations.AlterField(
            model_name='configure',
            name='gyo_fchoice',
            field=models.IntegerField(default=1),
        ),
        migrations.AlterField(
            model_name='configure',
            name='gyo_scale',
            field=models.IntegerField(default=2),
        ),
        migrations.AlterField(
            model_name='configure',
            name='listened_data_COUNT',
            field=models.IntegerField(default=700),
        ),
        migrations.AlterField(
            model_name='configure',
            name='listened_data_SLOP',
            field=models.IntegerField(default=400),
        ),
        migrations.AlterField(
            model_name='configure',
            name='listened_data_STABLECNT',
            field=models.IntegerField(default=300),
        ),
        migrations.AlterField(
            model_name='configure',
            name='open_angle_cnt',
            field=models.IntegerField(default=500),
        ),
        migrations.AlterField(
            model_name='configure',
            name='open_angle_threshold',
            field=models.IntegerField(default=30),
        ),
        migrations.AlterField(
            model_name='configure',
            name='split_data_MEAN_WIDTH_1',
            field=models.IntegerField(default=20),
        ),
        migrations.AlterField(
            model_name='configure',
            name='split_data_MEAN_WIDTH_2',
            field=models.IntegerField(default=10),
        ),
        migrations.AlterField(
            model_name='configure',
            name='split_data_VAR_LEN',
            field=models.IntegerField(default=3),
        ),
        migrations.AlterField(
            model_name='configure',
            name='split_data_WIDTH',
            field=models.IntegerField(default=20),
        ),
        migrations.AlterField(
            model_name='configure',
            name='update_middlevalue_cnt',
            field=models.IntegerField(default=5000),
        ),
        migrations.AlterField(
            model_name='configure',
            name='update_time',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
    ]
