# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('manhole_database', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Configure',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('relayid', models.CharField(default=b'0', max_length=30, null=True)),
                ('sensorid', models.CharField(default=b'0', max_length=10)),
                ('update_time', models.DateTimeField(verbose_name=b'date published')),
                ('acc_scale', models.IntegerField(default=0, null=True)),
                ('acc_fchoice', models.IntegerField(default=0, null=True)),
                ('acc_dlpf', models.IntegerField(default=0, null=True)),
                ('gyo_scale', models.IntegerField(default=0, null=True)),
                ('gyo_fchoice', models.IntegerField(default=0, null=True)),
                ('gyo_dlpf', models.IntegerField(default=0, null=True)),
                ('split_data_VAR_LEN', models.IntegerField(default=0, null=True)),
                ('split_data_MEAN_WIDTH_1', models.IntegerField(default=0, null=True)),
                ('split_data_MEAN_WIDTH_2', models.IntegerField(default=0, null=True)),
                ('get_valid_data_WIDTH', models.IntegerField(default=0, null=True)),
                ('split_data_WIDTH', models.IntegerField(default=0, null=True)),
                ('update_middlevalue_cnt', models.IntegerField(default=0, null=True)),
                ('listened_data_STABLECNT', models.IntegerField(default=0, null=True)),
                ('listened_data_SLOP', models.IntegerField(default=0, null=True)),
                ('listened_data_COUNT', models.IntegerField(default=0, null=True)),
                ('open_angle_threshold', models.IntegerField(default=0, null=True)),
                ('open_angle_cnt', models.IntegerField(default=0, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Configure_Log',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('target_relayid', models.CharField(default=b'0', max_length=30, null=True)),
                ('target_sensorid', models.CharField(default=b'0', max_length=30, null=True)),
                ('time', models.DateTimeField(verbose_name=django.utils.timezone.now)),
                ('finish_time', models.DateTimeField(default=django.utils.timezone.now)),
                ('finished', models.BooleanField(default=False)),
            ],
        ),
        migrations.CreateModel(
            name='Data',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('relayid', models.CharField(default=b'0', max_length=30)),
                ('sensorid', models.CharField(default=b'0', max_length=10)),
                ('update_time', models.DateTimeField(verbose_name=b'date published')),
                ('processed_status', models.IntegerField(default=0)),
                ('start_index', models.IntegerField(default=0)),
                ('end_index', models.IntegerField(default=0)),
                ('index_len', models.IntegerField(default=0)),
                ('width', models.IntegerField(default=0)),
                ('peakvalue', models.IntegerField(default=0)),
                ('other_peak', models.IntegerField(default=0)),
                ('other_var', models.IntegerField(default=0)),
            ],
        ),
        migrations.CreateModel(
            name='IPTables',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('relayid', models.CharField(default=b'0', max_length=30, null=True)),
                ('sensorid', models.CharField(default=b'0', max_length=10)),
                ('net_address', models.CharField(default=b'0', max_length=6, null=True)),
                ('channel', models.CharField(default=b'40', max_length=3, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Sensor',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('relayid', models.CharField(default=b'0', max_length=30, null=True)),
                ('sensorid', models.CharField(default=b'0', max_length=30)),
                ('update_time', models.DateTimeField(default=b'2016-04-07 10:58:41')),
                ('new', models.BooleanField()),
                ('open_time', models.DateTimeField(default=b'2016-04-07 10:58:41')),
                ('close_time', models.DateTimeField(default=b'2016-04-07 10:58:41')),
                ('status', models.CharField(default=b'closed', max_length=10)),
                ('period', models.CharField(default=b'0', max_length=10)),
                ('working_mode', models.CharField(default=b'0', max_length=10)),
                ('install_time', models.DateTimeField(verbose_name=b'date published')),
                ('max_speed', models.IntegerField(default=50)),
                ('heavy_vehicle_p', models.IntegerField(default=0)),
                ('light_vehicle_p', models.IntegerField(default=0)),
                ('manhole_material', models.CharField(default=b'unknown', max_length=10)),
                ('manhole_used_time', models.IntegerField(default=0)),
                ('estimate_status', models.CharField(default=b'low', max_length=10)),
                ('identified_status', models.FloatField(default=0.0, null=True)),
                ('heavy_vehicle_cnt', models.BigIntegerField(default=0, null=True)),
                ('middle_vehicle_cnt', models.BigIntegerField(default=0, null=True)),
                ('light_vehicle_cnt', models.BigIntegerField(default=0, null=True)),
                ('total_vehicle_cnt', models.BigIntegerField(default=0, null=True)),
                ('average_speed', models.IntegerField(default=50, null=True)),
                ('battery', models.FloatField(default=0.0, null=True)),
                ('open_status', models.CharField(default=b'0', max_length=10, null=True)),
                ('loss_status', models.CharField(default=b'0', max_length=10, null=True)),
                ('remarks', models.TextField(default=b'', null=True)),
                ('error', models.TextField(default=b'', null=True)),
            ],
        ),
        migrations.CreateModel(
            name='SensorData',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('relayid', models.CharField(default=b'0', max_length=30)),
                ('sensorid', models.CharField(default=b'0', max_length=10)),
                ('update_time', models.DateTimeField(verbose_name=b'date published')),
            ],
        ),
        migrations.DeleteModel(
            name='ParkData',
        ),
    ]
