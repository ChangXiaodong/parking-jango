# coding=utf-8
from django.shortcuts import render, render_to_response, RequestContext
from django.http import HttpResponse, HttpResponseRedirect
from info.models import ManholeData, ManholeDataHistory
from manhole_database.models import Sensor
from django.utils import timezone
import urllib
import urllib2
import json
import time
try:
    from django.http import JsonResponse
except ImportError:
    from .tool import JsonResponse

def index(req):
    level_enum = {"low": "低", "middle": "中", "high": "高", "unknow": "未知"}
    address = int(req.GET.get("id"))
    item = Sensor.objects.get(sensorid=address)
    datadic = {}
    datadic['address'] = address
    datadic['id'] = address
    status = str(item.identified_status)
    datadic['level'] = level_enum[status]
    datadic["open_status"] = item.open_status
    datadic["loss_status"] = item.loss_status
    datadic['time'] = (str(item.update_time.strftime('%Y-%m-%d %H:%M:%S')))

    return render_to_response('info/homepage/manholeconfig.html', {'datadic': datadic})


def update_threshold(req):

    address = int(req.GET.get("id"))
    # try:
    item = ManholeData.objects.filter(address=address)
    threshold = ManholeData.objects.get(address=address).TMR_data
    # except ManholeData.DoesNotExist, err:
    #     return render_to_response('info/homepage/manholeconfig.html')
    item.update(
        threshold=threshold
    )
    return JsonResponse({})
