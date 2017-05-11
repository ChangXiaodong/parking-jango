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


def getManholeItem(req):
    data = []
    address = int(req.GET.get("id"))
    dict = {}
    item = ManholeData.objects.get(address=address)
    dict['id'] = address
    dict['TMR_data'] = int(item.TMR_data)
    dict['reed_data'] = int(item.reed_data)
    dict['rssi_data'] = int(item.rssi_data)
    dict['snr_data'] = int(item.snr_data)
    dict['battery_data'] = int(item.battery_data)
    dict['threshold'] = int(item.threshold)
    dict['time'] = (str(item.update_time.strftime('%Y-%m-%d %H:%M:%S')))
    dict['cmd'] = int(item.command)
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