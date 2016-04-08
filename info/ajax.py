from django.http import HttpResponse
from django.shortcuts import render

try:
    from django.http import JsonResponse
except ImportError:
    from .tool import JsonResponse

import json
from info.models import ParkData, ParkDataHistory
from info.models import ManholeData, ManholeDataHistory

def getParking(request):
    data = []

    for i in range(1, 28):
        dict = {}
        item = ParkData.objects.get(nodeid="0086-110108-00022105-" + str(i).zfill(4))
        dict['id'] = str(i).zfill(4)
        dict['data'] = int(item.data)
        dict['time'] = (str(item.changed_time.strftime('%Y-%m-%d %H:%M:%S')))
        data.append(dict)
    sort = sorted(data, key=lambda a: a['time'],reverse=True)

    return JsonResponse(sort, safe=False)

def getManhole(request):
    data = []
    for i in range(1, 11):
        dict = {}
        item = ManholeData.objects.get(nodeid=str(i).zfill(4))
        dict['id'] = str(i).zfill(4)
        dict['data'] = int(item.data)
        dict['time'] = (str(item.changed_time.strftime('%Y-%m-%d %H:%M:%S')))
        data.append(dict)
    sort = sorted(data, key=lambda a: a['time'],reverse=True)

    return JsonResponse(sort, safe=False)

def getManholeItem(req):
    data = []
    nodeid = str(req.GET.get("id"))
    dict = {}
    item = ManholeData.objects.get(nodeid=nodeid)
    dict['id'] = nodeid
    dict['data'] = int(item.data)
    dict['time'] = (str(item.update_time.strftime('%Y-%m-%d %H:%M:%S')))
    dict['cmd'] = int(item.command)
    data.append(dict)
    return JsonResponse(data, safe=False)

def cmd_manhole(req):
    nodeid = req.GET.get("num")
    cmd = req.GET.get("cmd")
    ManholeData.objects.filter(nodeid=nodeid).update(
            command=cmd
        )
    return JsonResponse({})
