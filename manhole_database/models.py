# coding=utf-8
from django.db import models


# Create your models here.
class Sensor(models.Model):
    relayid = models.CharField(max_length=30, null=True, default='0')  # 中继id
    sensorid = models.CharField(max_length=30, default='0', primary_key=True)  # 传感器id
    update_time = models.DateTimeField('date published')
    new = models.BooleanField(default=True)  # 是否是新节点
    # 启动控制
    open_time = models.DateTimeField('date published')  # 传感器开启时间
    close_time = models.DateTimeField('date published')  # 传感器关闭时间
    period = models.CharField(max_length=30, null=True, default='0')  # 周期性开启的周期
    manual = models.CharField(max_length=10, null=True, default='0')
    # 工作模式
    # 'period':周期工作模式，周期由period设定
    # 'bytime':按照开启和关闭时间
    # 'manual':手动控制，由manual字段控制
    working_mode = models.CharField(max_length=10, null=True, default='0')
    # 其他手动配置参数
    install_time = models.DateTimeField('date published')  # 传感器安装时间

    # 算法数据
    # 手动配置

    max_speed = models.IntegerField(null=True, default=50)  # 交通正常时车辆平均车速
    heavy_vehicle_p = models.IntegerField(null=True, default=0)  # 载重车辆通过的概率
    light_vehicle_p = models.IntegerField(null=True, default=0)  # 自行车等车辆通过的概率
    manhole_material = models.CharField(max_length=10, null=True, default='unknown')  # 井盖材料
    manhole_installed_time = models.IntegerField(null=True, default=0)  # 井盖已经实用的时间，以天为单位
    estimate_status = models.CharField(max_length=10, null=True, default='low')  # 井盖损坏程度预估，low，middle，high

    # 识别参数
    identified_status = models.FloatField(null=True, default=0.0)  # 测量出的损坏程度，百分比
    heavy_vehicle_cnt = models.BigIntegerField(null=True, default=0)  # 重型车辆通过数量
    middle_vehicle_cnt = models.BigIntegerField(null=True, default=0)  # 中型车辆通过数量
    light_vehicle_cnt = models.BigIntegerField(null=True, default=0)  # 小型车辆通过数量
    total_vehicle_cnt = models.BigIntegerField(null=True, default=0)  # 通过车辆总个数，除大中小外可能包含其他离散的车辆
    average_speed = models.IntegerField(null=True, default=50)  # 根据人工设定的速度，网上抓取的速度，算法识别的速度。综合判断得到的速度

    battery = models.FloatField(null=True, default=0.0)  # 剩余电量
    open_status = models.CharField(max_length=10, null=True, default='0')  # 开启状态
    loss_status = models.CharField(max_length=10, null=True, default='0')  # 丢失状态

    # 其他参数
    remarks = models.TextField(null=True, default='')
    error = models.TextField(null=True, default='')


class Data(models.Model):
    relayid = models.CharField(max_length=30, null=True, default='0')  # 中继id
    sensorid = models.ForeignKey(Sensor, related_name='data_sensor_id', default="0")  # 传感器id
    update_time = models.DateTimeField('date published')  # 数据更新时间
    processed_status = models.IntegerField(default=0)  # 数据被处理的次数

    start_index = models.IntegerField(default=0)  # 波形起始位置
    end_index = models.IntegerField(default=0)  # 波形中止位置
    max_index = models.CharField(max_length=100, null=True, default='')  # 最大值对应的index
    min_index = models.CharField(max_length=100, null=True, default='')  # 最小值对应的index
    acc_z_max = models.IntegerField(default=0)  # 加速度z轴波形最大值
    acc_z_min = models.IntegerField(default=0)  # 加速度z轴波形最小值
    acc_x_var = models.CharField(max_length=10, default="0")  # 加速度x轴方差，抖动情况
    acc_y_var = models.CharField(max_length=10, default="0")  # 加速度y轴方差，抖动情况
    gyo_x_var = models.CharField(max_length=10, default="0")  # 陀螺仪x轴方差，抖动情况
    gyo_y_var = models.CharField(max_length=10, default="0")  # 陀螺仪y轴方差，抖动情况
    gyo_z_var = models.CharField(max_length=10, default="0")  # 陀螺仪z轴方差，抖动情况


class Configure(models.Model):
    relayid = models.CharField(max_length=30, null=True, default='0')  # 中继id
    sensorid = models.ForeignKey(Sensor, related_name='configure_sensor_id', default="0")  # 传感器id
    update_time = models.DateTimeField('date published')  # 数据更新时间

    # 传感器参数配置
    acc_scale = models.IntegerField(null=True, default=0)
    acc_fchoice = models.IntegerField(null=True, default=0)
    acc_dlpf = models.IntegerField(null=True, default=0)
    gyo_scale = models.IntegerField(null=True, default=0)
    gyo_fchoice = models.IntegerField(null=True, default=0)
    gyo_dlpf = models.IntegerField(null=True, default=0)

class Configure_Log(models.Model):
    target_relayid = models.CharField(max_length=30, null=True, default='0')  # 中继id
    target_sensorid = models.CharField(max_length=30, null=True, default='0')  # 传感器id
    time = models.DateTimeField('date published')  # 数据更新时间
    finish_time = models.DateTimeField('date published')
    finished = models.BooleanField(default=False)

