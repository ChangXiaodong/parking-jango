# coding=utf-8
from django.http import HttpResponse
from django.shortcuts import render
import os
import platform
import time
import urllib
import urllib2
import socket

try:
    from django.http import JsonResponse
except ImportError:
    from .tool import JsonResponse

import json
from info.models import ParkData, ParkDataHistory
from info.models import ManholeData, ManholeDataHistory
from info.models import BillBoardData

from manhole_database.models import Sensor


def getParking(request):
    data = []
    for i in range(1, 28):
        dict = {}
        item = ParkData.objects.get(nodeid="0086-110108-00022105-" + str(i).zfill(4))
        dict['id'] = str(i).zfill(4)
        dict['data'] = int(item.data)
        dict['time'] = (str(item.changed_time.strftime('%Y-%m-%d %H:%M:%S')))
        data.append(dict)
    sort = sorted(data, key=lambda a: a['time'], reverse=True)
    return JsonResponse(sort, safe=False)


def getParkingItem(req):
    print("empty")
    data = []
    nodeid = str(req.GET.get("id"))
    dict = {}
    item = ParkData.objects.get(nodeid=nodeid)
    dict['id'] = nodeid
    dict['data'] = int(item.data)
    dict['time'] = (str(item.time.strftime('%Y-%m-%d %H:%M:%S')))
    dict['cmd'] = int(item.command)
    data.append(dict)
    return JsonResponse(data, safe=False)


def getManhole(request):
    data = []
    for i in range(1, 10):
        dict = {}
        item = ManholeData.objects.get(address=i)
        dict['id'] = i
        dict['TMR_data'] = int(item.TMR_data)
        dict['reed_data'] = int(item.reed_data)
        dict['rssi_data'] = int(item.rssi_data)
        dict['snr_data'] = int(item.snr_data)
        dict['battery_data'] = int(item.battery_data)
        dict['threshold'] = int(item.threshold)
        dict['time'] = (str(item.changed_time.strftime('%Y-%m-%d %H:%M:%S')))
        data.append(dict)

    sort = sorted(data, key=lambda a: a['time'], reverse=True)

    return JsonResponse(sort, safe=False)


def getManhole_new(request):
    data = []
    for i in range(1, 21):
        level_enum = {"low": "低", "middle": "中", "high": "高", "unknow": "未知"}
        dict = {}
        item = Sensor.objects.get(sensorid=i)
        dict['id'] = i
        status = str(item.identified_status)
        dict['level'] = level_enum[status]
        dict["open_status"] = item.open_status
        dict["loss_status"] = item.loss_status
        dict['time'] = (str(item.update_time.strftime('%Y-%m-%d %H:%M:%S')))
        data.append(dict)

    # sort = sorted(data, key=lambda a: a['time'], reverse=True)

    return JsonResponse(data, safe=False)


def getManholeItem(req):
    level_enum = {"low": "低", "middle": "中", "high": "高", "unknow": "未知"}
    data = []
    id = int(req.GET.get("id"))
    dict = {}
    item = Sensor.objects.get(sensorid=id)
    dict['id'] = id
    status = str(item.identified_status)
    dict['level'] = level_enum[status]
    dict['level_num'] = item.level_percent
    dict["open_status"] = item.open_status
    dict["loss_status"] = item.loss_status
    percent = int((float((1500 - float(item.battery)) / 120)) * 100)
    percent = min(100, percent)
    dict["battery"] = "{}".format(percent)
    dict['time'] = (str(item.update_time.strftime('%Y-%m-%d %H:%M:%S')))
    data.append(dict)
    return JsonResponse(data, safe=False)


def cmd_manhole(req):
    address = req.GET.get("num")
    cmd = req.GET.get("cmd")
    ManholeData.objects.filter(address=address).update(
        command=cmd
    )
    return JsonResponse({})


def getBillboard(request):
    data = []
    for i in range(1, 11):
        dict = {}
        item = BillBoardData.objects.get(nodeid=str(i).zfill(4))
        dict['id'] = str(i).zfill(4)
        dict['x'] = str(item.x)
        dict['y'] = str(item.y)
        data.append(dict)

    return JsonResponse(data, safe=False)
