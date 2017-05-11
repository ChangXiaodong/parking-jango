# coding=utf-8
from django.http import HttpResponse
from manhole_database.models import Data
from manhole_database.models import Sensor
from manhole_database.models import Configure
from manhole_database.models import PreConfigure
from manhole_database.models import IPTables
from manhole_database.models import RelayConfig
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
            res = {}
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
            res = {}
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
                    minutes = (q.close_time - time_now).seconds / 60
                    node["open"].append({q.sensorid: minutes})
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


def params_set(req):
    if req.method == 'POST':
        status = req.POST["status"]
        if status == "update":
            params_index = {
                "split_data_VAR_LEN": 1,
                "split_data_MEAN_WIDTH_1": 2,
                "split_data_MEAN_WIDTH_2": 3,
                "get_valid_data_WIDTH": 4,
                "split_data_WIDTH": 5,
                "update_middlevalue_cnt": 6,
                "listened_data_STABLECNT": 7,
                "listened_data_SLOP": 8,
                "listened_data_COUNT": 9,
                "open_angle_threshold": 10,
                "open_angle_cnt": 11,
                "acc_scale": 12,
                "acc_fchoice": 13,
                "acc_dlpf": 14,
                "gyo_scale": 15,
                "gyo_fchoice": 16,
                "gyo_dlpf": 17
            }
            sensor_id_set = [q.sensorid for q in PreConfigure.objects.filter(relayid=req.POST["relayid"])]
            pre_params = {}
            for id in sensor_id_set:
                buf = {}
                pre_sensor = PreConfigure.objects.get(sensorid=id)
                cur_sensor = Configure.objects.get(sensorid=id)
                if pre_sensor.acc_scale != cur_sensor.acc_scale:
                    buf[params_index["acc_scale"]] = pre_sensor.acc_scale
                if pre_sensor.acc_fchoice != cur_sensor.acc_fchoice:
                    buf[params_index["acc_fchoice"]] = pre_sensor.acc_fchoice
                if pre_sensor.acc_dlpf != cur_sensor.acc_dlpf:
                    buf[params_index["acc_dlpf"]] = pre_sensor.acc_dlpf
                if pre_sensor.gyo_scale != cur_sensor.gyo_scale:
                    buf[params_index["gyo_scale"]] = pre_sensor.gyo_scale
                if pre_sensor.gyo_fchoice != cur_sensor.gyo_fchoice:
                    buf[params_index["gyo_fchoice"]] = pre_sensor.gyo_fchoice
                if pre_sensor.gyo_dlpf != cur_sensor.gyo_dlpf:
                    buf[params_index["gyo_dlpf"]] = pre_sensor.gyo_dlpf
                if pre_sensor.split_data_VAR_LEN != cur_sensor.split_data_VAR_LEN:
                    buf[params_index["split_data_VAR_LEN"]] = pre_sensor.split_data_VAR_LEN
                if pre_sensor.split_data_MEAN_WIDTH_1 != cur_sensor.split_data_MEAN_WIDTH_1:
                    buf[params_index["split_data_MEAN_WIDTH_1"]] = pre_sensor.split_data_MEAN_WIDTH_1
                if pre_sensor.split_data_MEAN_WIDTH_2 != cur_sensor.split_data_MEAN_WIDTH_2:
                    buf[params_index["split_data_MEAN_WIDTH_2"]] = pre_sensor.split_data_MEAN_WIDTH_2
                if pre_sensor.get_valid_data_WIDTH != cur_sensor.get_valid_data_WIDTH:
                    buf[params_index["get_valid_data_WIDTH"]] = pre_sensor.get_valid_data_WIDTH
                if pre_sensor.split_data_WIDTH != cur_sensor.split_data_WIDTH:
                    buf[params_index["split_data_WIDTH"]] = pre_sensor.split_data_WIDTH
                if pre_sensor.update_middlevalue_cnt != cur_sensor.update_middlevalue_cnt:
                    buf[params_index["update_middlevalue_cnt"]] = pre_sensor.update_middlevalue_cnt
                if pre_sensor.listened_data_STABLECNT != cur_sensor.listened_data_STABLECNT:
                    buf[params_index["listened_data_STABLECNT"]] = pre_sensor.listened_data_STABLECNT
                if pre_sensor.listened_data_SLOP != cur_sensor.listened_data_SLOP:
                    buf[params_index["listened_data_SLOP"]] = pre_sensor.listened_data_SLOP
                if pre_sensor.listened_data_COUNT != cur_sensor.listened_data_COUNT:
                    buf[params_index["listened_data_COUNT"]] = pre_sensor.listened_data_COUNT
                if pre_sensor.open_angle_threshold != cur_sensor.open_angle_threshold:
                    buf[params_index["open_angle_threshold"]] = pre_sensor.open_angle_threshold
                if pre_sensor.open_angle_cnt != cur_sensor.open_angle_cnt:
                    buf[params_index["open_angle_cnt"]] = pre_sensor.open_angle_cnt
                if buf:
                    pre_params[id] = buf

            return HttpResponse(json.dumps(pre_params), content_type="application/json")
        else:
            index = int(req.POST["index"])
            sensor_id = req.POST["sensor_id"]
            value = req.POST["value"]

            obj = Configure.objects.filter(sensorid=sensor_id)
            if index == 1:
                obj.update(split_data_VAR_LEN=value)
            elif index == 2:
                obj.update(split_data_MEAN_WIDTH_1=value)
            elif index == 3:
                obj.update(split_data_MEAN_WIDTH_2=value)
            elif index == 4:
                obj.update(get_valid_data_WIDTH=value)
            elif index == 5:
                obj.update(split_data_WIDTH=value)
            elif index == 6:
                obj.update(update_middlevalue_cnt=value)
            elif index == 7:
                obj.update(listened_data_STABLECNT=value)
            elif index == 8:
                obj.update(listened_data_SLOP=value)
            elif index == 9:
                obj.update(listened_data_COUNT=value)
            elif index == 10:
                obj.update(open_angle_threshold=value)
            elif index == 11:
                obj.update(open_angle_cnt=value)
            elif index == 12:
                obj.update(acc_scale=value)
            elif index == 13:
                obj.update(acc_fchoice=value)
            elif index == 14:
                obj.update(acc_dlpf=value)
            elif index == 15:
                obj.update(gyo_scale=value)
            elif index == 16:
                obj.update(gyo_fchoice=value)
            elif index == 17:
                obj.update(gyo_dlpf=value)

            return HttpResponse(json.dumps("ok"), content_type="application/json")


def open_status(req):
    if req.method == 'POST':
        sensor_id = req.POST.get("sensor_id")
        open_status = req.POST.get("open_status")
        Sensor.objects.filter(sensorid=sensor_id).update(
            open_status=open_status
        )
        return HttpResponse(json.dumps("ok"), content_type="application/json")


def heart_beat(req):
    if req.method == 'POST':
        sensor_id = req.POST.get("sensor_id")
        battery = float(req.POST.get("battery"))
        battery = "{:.2f}%".format((1550.0 - battery) / 2)
        Sensor.objects.filter(sensorid=sensor_id).update(
            battery=battery,
            update_time=timezone.now()
        )
        return HttpResponse(json.dumps("ok"), content_type="application/json")


def relay_start(req):
    if req.method == 'POST':
        relay_id = req.POST.get("relay_id")
        relay_data_object = RelayConfig.objects.filter(relayid=relay_id)
        relay_data_object.update(
            start_time=timezone.now()
        )
        local_port = ""
        remote_port = ""
        for q in relay_data_object:

            local_port = q.local_port
            remote_port = q.remote_port
        data = {"local_port": local_port, "remote_port": remote_port}

        return HttpResponse(json.dumps(data), content_type="application/json")
