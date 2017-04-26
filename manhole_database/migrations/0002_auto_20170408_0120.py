# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('manhole_database', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='ManholeDatabaseData',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('relayid', models.CharField(default=b'0', max_length=30, null=True)),
                ('sensorid', models.CharField(default=b'0', max_length=30, null=True)),
                ('update_time', models.DateTimeField(verbose_name=b'date published')),
                ('processed_status', models.IntegerField(default=0)),
                ('start_index', models.IntegerField(default=0)),
                ('end_index', models.IntegerField(default=0)),
                ('max_index', models.CharField(default=b'', max_length=100, null=True)),
                ('min_index', models.CharField(default=b'', max_length=100, null=True)),
                ('acc_z_max', models.IntegerField(default=0)),
                ('acc_z_min', models.IntegerField(default=0)),
                ('acc_x_var', models.CharField(default=b'0', max_length=10)),
                ('acc_y_var', models.CharField(default=b'0', max_length=10)),
                ('gyo_x_var', models.CharField(default=b'0', max_length=10)),
                ('gyo_y_var', models.CharField(default=b'0', max_length=10)),
                ('gyo_z_var', models.CharField(default=b'0', max_length=10)),
            ],
        ),
        migrations.CreateModel(
            name='ManholeDatabaseSensor',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('relayid', models.CharField(default=b'0', max_length=30, null=True)),
                ('sensorid', models.CharField(default=b'0', max_length=30, null=True)),
                ('update_time', models.DateTimeField(verbose_name=b'date published')),
                ('open_time', models.DateTimeField(verbose_name=b'date published')),
                ('close_time', models.DateTimeField(verbose_name=b'date published')),
                ('period', models.CharField(default=b'0', max_length=30, null=True)),
                ('manual', models.CharField(default=b'0', max_length=10, null=True)),
                ('working_mode', models.CharField(default=b'0', max_length=10, null=True)),
                ('install_time', models.DateTimeField(verbose_name=b'date published')),
                ('max_speed', models.IntegerField(default=50, null=True)),
                ('heavy_vehicle_p', models.IntegerField(default=0, null=True)),
                ('light_vehicle_p', models.IntegerField(default=0, null=True)),
                ('manhole_material', models.CharField(default=b'unknown', max_length=10, null=True)),
                ('manhole_installed_time', models.IntegerField(default=0, null=True)),
                ('estimate_status', models.CharField(default=b'low', max_length=10, null=True)),
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
            name='ManholeDatabaseSensorConfigure',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('relayid', models.CharField(default=b'0', max_length=30, null=True)),
                ('sensorid', models.CharField(default=b'0', max_length=30, null=True)),
                ('update_time', models.DateTimeField(verbose_name=b'date published')),
                ('acc_scale', models.IntegerField(default=0, null=True)),
                ('acc_fchoice', models.IntegerField(default=0, null=True)),
                ('acc_dlpf', models.IntegerField(default=0, null=True)),
                ('gyo_scale', models.IntegerField(default=0, null=True)),
                ('gyo_fchoice', models.IntegerField(default=0, null=True)),
                ('gyo_dlpf', models.IntegerField(default=0, null=True)),
            ],
        ),
        migrations.DeleteModel(
            name='ManholeDatabaseHistory',
        ),
    ]
