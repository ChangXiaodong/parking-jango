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
    testid = []
    for i in range(1, 28):
        dict = {}
        item = ParkData.objects.get(nodeid="0086-110108-00022105-" + str(i).zfill(4))
        dict['id'] = str(i).zfill(4)
        dict['data'] = int(item.data)
        dict['time'] = (str(item.changed_time.strftime('%Y-%m-%d %H:%M:%S')))
        data.append(dict)
    sort = sorted(data, key=lambda a: a['time'], reverse=True)
    for i in sort:
        if i in testid:
            print i
        else:
            testid.append(i['id'])
    item = ParkDataHistory.objects.order_by("-id")[0]
    if platform.system() == "Linux":
        root_audio_dir = "./static/audios/"
    else:
        root_audio_dir = "./common_static/audios/"
    timestap = time.mktime(time.strptime(str(item.time), '%Y-%m-%d %H:%M:%S'))
    if abs(timestap - time.time()) < 10:
        record = str(item.record)
        if request.META.has_key('HTTP_X_FORWARDED_FOR'):
            myaddr = request.META['HTTP_X_FORWARDED_FOR']
        else:
            myaddr = request.META['REMOTE_ADDR']

        if myaddr not in record or abs(timestap - time.time()) < 1:
            ParkDataHistory.objects.filter(time=item.time).update(
                # record={myname: myaddr}
                record=str(item.record) + str({myaddr})
            )
            nocar_id = ""
            car_id = ""
            offline_id = ""
            voice = ""
            changed_node = sorted(eval(item.data).items(), key=lambda d: d[0])
            for key, value in changed_node:
                key = key[-4:]
                if value == "0":
                    nocar_id += key + ","
                elif value == "1":
                    car_id += key + ","
                elif value == "253":
                    offline_id += key + ","
            if nocar_id != "":
                nocar_id = nocar_id[:-1] + "未停车"
                voice += nocar_id
            if car_id != "":
                car_id = car_id[:-1] + "已停车"
                voice += car_id
            if offline_id != "":
                offline_id = offline_id[:-1] + "掉线"
                voice += offline_id
            voice_data = {"tex": voice,
                          "lan": "zh",
                          "tok": "24.1f8aa4a8d6cc26624ac0c95ca41cbc36.2592000.1463304322.282335-8008822",
                          "ctp": "1",
                          "cuid": "123456789",
                          "spd": "5",
                          "pit": "5",
                          "vol": "5",
                          "per": "0"}
            post_data = urllib.urlencode(voice_data)
            response = urllib2.urlopen("http://tsn.baidu.com/text2audio", post_data, timeout=3)
            voicename = str(time.time())

            with open(root_audio_dir + voicename, "wb") as v:
                v.write(response.read())
            sort.append({'data': 0, 'id': '0000', 'time': '200-00-00 00:00:00', 'voice': "/static/audios/" + voicename})
    voice_content_list = os.listdir(root_audio_dir)
    for f in voice_content_list:
        filepath = os.path.join(root_audio_dir, f)
        if os.path.isfile(filepath) and float(time.time()) - float(f.split(".")[0]) > 120:
            filepath = os.path.join(root_audio_dir, f)
            os.remove(filepath)
    return JsonResponse(sort, safe=False)


def getParkingItem(req):
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