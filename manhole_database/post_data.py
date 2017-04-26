# coding=utf-8
from django.http import HttpResponse
from manhole_database.models import Data
from manhole_database.models import Sensor
from manhole_database.models import Configure
from manhole_database.models import IPTables
import json
from django.utils import timezone


def post_sensor_data(req):
    if req.method == 'POST':
        # dataandid = req.POST.get("data")
        print("received")
        print(req.POST)
        return HttpResponse(json.dumps(req.POST), content_type="application/json")
    if req.method == 'GET':
        return HttpResponse(json.dumps(req.GET), content_type="application/json")


def get_iptables(req):
    if req.method == 'POST':
        relayid = req.POST.get("relayid")
        try:
            quary = IPTables.objects.filter(relayid=relayid)
            res = [{"len": str(len(quary))}]
            for q in quary:
                res.append({"n_a": str(q.net_address), "s_i": q.sensorid.sensorid})
        except:
            res = {"res": "empty"}
        res = json.dumps(res)
        return HttpResponse(res, content_type="application/json")
