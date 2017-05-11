# coding=utf-8
from django.db import models
from django.utils import timezone


# Create your models here.
class Sensor(models.Model):
    relayid = models.CharField(max_length=30, null=True, default='0')  # 中继id
    sensorid = models.CharField(max_length=30, default='0')  # 传感器id
    update_time = models.DateTimeField(default='2016-04-07 10:58:41')
    new = models.BooleanField()  # 是否是新节点
    # 启动控制
    open_time = models.DateTimeField(default='2016-04-07 10:58:41')  # 传感器开启时间
    close_time = models.DateTimeField(default='2016-04-07 10:58:41')  # 传感器关闭时间
    status = models.CharField(max_length=10, default="closed")  # 当前开启状态
    period = models.CharField(max_length=10, default='0')  # 周期性开启的周期
    # 工作模式
    # 'period':周期工作模式，周期由period设定
    # 'bytime':按照开启和关闭时间
    # 'manual':手动控制，由manual字段控制
    working_mode = models.CharField(max_length=10, default='0')
    # 其他手动配置参数
    install_time = models.DateTimeField('date published')  # 传感器安装时间

    # 算法数据
    # 手动配置

    max_speed = models.IntegerField(default=50)  # 交通正常时车辆平均车速
    heavy_vehicle_p = models.IntegerField(default=0)  # 载重车辆通过的概率
    light_vehicle_p = models.IntegerField(default=0)  # 自行车等车辆通过的概率
    manhole_material = models.CharField(max_length=10, default='unknown')  # 井盖材料
    manhole_used_time = models.IntegerField(default=0)  # 井盖已经实用的时间，以天为单位
    estimate_status = models.CharField(max_length=10, default='low')  # 井盖损坏程度预估，low，middle，high

    # 识别参数
    identified_status = models.FloatField(null=True, default=0.0)  # 测量出的损坏程度，百分比
    heavy_vehicle_cnt = models.BigIntegerField(null=True, default=0)  # 重型车辆通过数量
    middle_vehicle_cnt = models.BigIntegerField(null=True, default=0)  # 中型车辆通过数量
    light_vehicle_cnt = models.BigIntegerField(null=True, default=0)  # 小型车辆通过数量
    total_vehicle_cnt = models.BigIntegerField(null=True, default=0)  # 通过车辆总个数，除大中小外可能包含其他离散的车辆
    average_speed = models.IntegerField(null=True, default=50)  # 根据人工设定的速度，网上抓取的速度，算法识别的速度。综合判断得到的速度

    battery = models.CharField(null=True, max_length=10, default="0")  # 剩余电量
    open_status = models.CharField(max_length=10, null=True, default='0')  # 开启状态
    loss_status = models.CharField(max_length=10, null=True, default='0')  # 丢失状态

    # 其他参数
    remarks = models.TextField(null=True, default='')
    error = models.TextField(null=True, default='')


class Data(models.Model):
    relayid = models.CharField(max_length=30, default='0')  # 中继id
    sensorid = models.CharField(max_length=10, default="0")  # 传感器id
    update_time = models.DateTimeField('date published')  # 数据更新时间
    processed_status = models.IntegerField(default=0)  # 数据被处理的次数

    start_index = models.IntegerField(default=0)  # 波形起始位置
    end_index = models.IntegerField(default=0)  # 波形中止位置
    index_len = models.IntegerField(default=0)  # 车辆轮子个数
    width = models.IntegerField(default=0)  # 车辆轴距
    peakvalue = models.IntegerField(default=0)  # 加速度z轴波形最大最小差值
    other_peak = models.IntegerField(default=0)  # 其他轴极值
    other_var = models.IntegerField(default=0)  # 其他轴方差


class Configure(models.Model):
    relayid = models.CharField(max_length=30, null=True, default='0')  # 中继id
    sensorid = models.CharField(max_length=10, default="0")  # 传感器id
    update_time = models.DateTimeField(default=timezone.now)  # 数据更新时间

    # 传感器参数配置
    acc_scale = models.IntegerField(default=0)
    acc_fchoice = models.IntegerField(default=0)
    acc_dlpf = models.IntegerField(default=5)
    gyo_scale = models.IntegerField(default=2)
    gyo_fchoice = models.IntegerField(default=1)
    gyo_dlpf = models.IntegerField(default=6)

    # 算法参数配置
    split_data_VAR_LEN = models.IntegerField(default=3)
    split_data_MEAN_WIDTH_1 = models.IntegerField(default=20)
    split_data_MEAN_WIDTH_2 = models.IntegerField(default=10)
    get_valid_data_WIDTH = models.IntegerField(default=2)
    split_data_WIDTH = models.IntegerField(default=20)
    update_middlevalue_cnt = models.IntegerField(default=5000)
    listened_data_STABLECNT = models.IntegerField(default=300)
    listened_data_SLOP = models.IntegerField(default=400)
    listened_data_COUNT = models.IntegerField(default=700)
    open_angle_threshold = models.IntegerField(default=30)
    open_angle_cnt = models.IntegerField(default=500)


class PreConfigure(models.Model):
    relayid = models.CharField(max_length=30, null=True, default='0')  # 中继id
    sensorid = models.CharField(max_length=10, default="0")  # 传感器id
    update_time = models.DateTimeField(default=timezone.now)  # 数据更新时间

    # 传感器参数配置
    acc_scale = models.IntegerField(default=0)
    acc_fchoice = models.IntegerField(default=0)
    acc_dlpf = models.IntegerField(default=5)
    gyo_scale = models.IntegerField(default=2)
    gyo_fchoice = models.IntegerField(default=1)
    gyo_dlpf = models.IntegerField(default=6)

    # 算法参数配置
    split_data_VAR_LEN = models.IntegerField(default=3)
    split_data_MEAN_WIDTH_1 = models.IntegerField(default=20)
    split_data_MEAN_WIDTH_2 = models.IntegerField(default=10)
    get_valid_data_WIDTH = models.IntegerField(default=2)
    split_data_WIDTH = models.IntegerField(default=20)
    update_middlevalue_cnt = models.IntegerField(default=5000)
    listened_data_STABLECNT = models.IntegerField(default=300)
    listened_data_SLOP = models.IntegerField(default=400)
    listened_data_COUNT = models.IntegerField(default=700)
    open_angle_threshold = models.IntegerField(default=30)
    open_angle_cnt = models.IntegerField(default=500)


class IPTables(models.Model):
    relayid = models.CharField(max_length=30, null=True, default='0')
    sensorid = models.CharField(max_length=10, default="0")
    net_address = models.CharField(max_length=6, null=True, default='0')
    channel = models.CharField(max_length=3, null=True, default='40')

class RelayConfig(models.Model):
    relayid = models.CharField(max_length=30, null=True, default='0')
    start_time = models.DateTimeField(default='2016-04-07 10:58:41')
    local_port = models.CharField(max_length=10, default="0")
    remote_port = models.CharField(max_length=10, default="0")
