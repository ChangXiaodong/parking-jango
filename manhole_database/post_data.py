# coding=utf-8
from django.http import HttpResponse
from manhole_database.models import Data
from manhole_database.models import Sensor
from manhole_database.models import Configure
from manhole_database.models import IPTables
import json
from django.utils import timezone
import datetime


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
        res = {}
        try:
            quary = IPTables.objects.filter(relayid=relayid)
            for q in quary:
                res[str(q.sensorid)] = [str(q.channel), str(q.net_address)]
        except:
            res = {"res": "empty"}
        res = json.dumps(res)
        return HttpResponse(res, content_type="application/json")


def get_new_nodes(req):
    if req.method == 'POST':
        relayid = req.POST.get("relayid")
        res = []
        try:
            quary = Sensor.objects.filter(relayid=relayid)
            for q in quary:
                if q.new == 1:
                    res.append(q.sensorid)
        except:
            res = {"res": "empty"}
        res = json.dumps(res)
        return HttpResponse(res, content_type="application/json")


def active_node(req):
    if req.method == 'POST':
        relayid = req.POST.get("relayid")
        node = {"open": [], "close": []}
        time_now = timezone.now()
        try:
            quary = Sensor.objects.filter(relayid=relayid)
            for q in quary:
                if q.open_time < time_now < q.close_time and q.status == "close":
                    node["open"].append(q.sensorid)
                if (q.open_time > time_now or time_now > q.close_time) and q.status == "open":

                    node["close"].append(q.sensorid)
        except:
            pass
        return HttpResponse(json.dumps(node), content_type="application/json")


def node_status(req):
    if req.method == 'POST':
        sensor_id = req.POST.get("sensor_id")
        status = req.POST.get("status")
        Sensor.objects.filter(sensorid=sensor_id).update(
            status=status
        )
        return HttpResponse(json.dumps("ok"), content_type="application/json")


def insert_data(req):
    if req.method == 'POST':
        start_index = int(req.POST["start_index"])
        end_index = int(req.POST["end_index"])
        index_len = int(req.POST["index_len"])
        width = int(req.POST["width"])
        peakvalue = int(req.POST["peakvalue"])
        other_peak = int(req.POST["other_peak"])
        other_var = int(req.POST["other_var"])
        sensor_id = req.POST["sensor_id"]
        relay_id = Sensor.objects.get(sensorid=sensor_id).relayid
        Sensor.objects.filter(sensorid=sensor_id).update(update_time=timezone.now())

        Data.objects.create(
            relayid=relay_id,
            sensorid=sensor_id,
            update_time=timezone.now(),
            processed_status=0,
            start_index=start_index,
            end_index=end_index,
            index_len=index_len,
            width=width,
            peakvalue=peakvalue,
            other_peak=other_peak,
            other_var=other_var
        )
        return HttpResponse(json.dumps("ok"), content_type="application/json")
