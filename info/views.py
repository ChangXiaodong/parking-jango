# coding=utf-8
from django.shortcuts import render, render_to_response, RequestContext
from django.http import HttpResponse, HttpResponseRedirect
from info.models import ParkData, ParkDataHistory
from info.models import ManholeData, ManholeDataHistory
from info.models import BillBoardData
from django.utils import timezone
import urllib
import urllib2
import json
import time


def index(req):
    # for i in range(1,51):
    #     ParkData.objects .create(time=timezone.now(),relayid="0086-110108-00022105-01", data="0", parkid="22105", nodeid="0086-110108-00022105-" + str(i).zfill(4))
    # return HttpResponse("Init Database")

    if req.method == 'POST':
        parkdata = {}
        post_data = ""
        dataandid = str(req.POST.get("data")).split(",")
        cmdStack = {}
        changed_flag = 0
        changed_node = {}
        for item in dataandid:
            parkdata["node_id"] = item.split("|")[0]
            parkdata["data"] = item.split("|")[1]
            parkdata["relay_id"] = str(req.POST.get("relay_id"))
            parkdata["park_id"] = str(req.POST.get("park_id"))

            item = ParkData.objects.get(nodeid=parkdata["node_id"])
            data_memory = str(item.data)
            cmd = str(item.command)
            ParkData.objects.filter(nodeid=parkdata["node_id"]).update(
                time=timezone.now(),
                relayid=parkdata["relay_id"],
                data=parkdata["data"],
                parkid=parkdata["park_id"]
            )

            if cmd != '0':
                cmdStack[parkdata["node_id"]] = cmd
                ParkData.objects.filter(nodeid=parkdata["node_id"]).update(command="0")
            if data_memory != parkdata["data"]:
                ParkData.objects.filter(nodeid=parkdata["node_id"]).update(
                    changed_time=timezone.now()
                )
                key = parkdata["node_id"]
                changed_node[key] = parkdata["data"]
                # if parkdata["data"] == "0" or parkdata["data"] == "1":
                #     changed_flag = 1
                #     post_data += parkdata["node_id"] + "|" + parkdata["data"] + ","
                #     parkdata["data"] = post_data[:-1]
        if changed_flag:
            pass
            # try:
            #     response = urllib2.urlopen("http://123.57.37.66:8080/sensor/post/status",
            #                                urllib.urlencode(parkdata),
            #                                timeout=1)
            #     cmdStack["Status"] = "Success"
            # except urllib2.HTTPError, err:
            #     return HttpResponse(err)
        else:
            cmdStack["Status"] = "Not Changed"

        if len(changed_node) != 0:
            ParkDataHistory.objects.create(
                time=timezone.now(),
                relayid=parkdata["relay_id"],
                data=changed_node,
                parkid=parkdata["park_id"],
                record=""
            )

        return HttpResponse(json.dumps(cmdStack), content_type="application/json")
    else:
        nodeid = req.GET.get("num")
        cmd = req.GET.get("cmd")
        with open("cmd_log.txt", 'a+') as file:
            file.write(
                time.strftime('%Y-%m-%d  %H:%M:%S', time.localtime(time.time())) + "  " + nodeid + "  " + cmd + "\n")
        ParkData.objects.filter(nodeid=nodeid).update(
            command=cmd
        )
        return HttpResponseRedirect('/info/cmd/')


def postmanhole(req):
    TMR_DATA           = 1
    REED_DATA          = 2
    CMD_DATA           = 3
    RSSI_DATA          = 4
    SNR_DATA           = 5
    BATTERY_DATA       = 6

    response={}
    request={}
    try:
        if req.method == 'POST':
            request['address'] = int(req.POST.get("address"))
            request['data_type'] = int(req.POST.get("data_type"))
            request['data'] = int(req.POST.get("data"))

        elif req.method == 'GET':
            request['address'] = int(req.GET.get("address"))
            request['data_type'] = int(req.GET.get("data_type"))
            request['data'] = int(req.GET.get("data"))
    except ValueError,err:
        response["status"] = "Failed"
        response["err"] = "data format error"
        return HttpResponse(json.dumps(response), content_type="application/json")

    ManholeDataHistory.objects.create(
                update_time=timezone.now(),
                address=request['address'],
                data=request['data'],
                data_type=request['data_type'],
                administrator="xiaoxiami",
                last_disable_time="2000-01-01 00:00:00"
            )

    item = ManholeData.objects.filter(address=request['address'])

    if request['data_type'] == TMR_DATA:
        item.update(
                update_time=timezone.now(),
                TMR_data=request['data'],
        )
    elif request['data_type'] == REED_DATA:
        item.update(
            update_time=timezone.now(),
            reed_data=request['data'],
        )
    elif request['data_type'] == RSSI_DATA:
        item.update(
            update_time=timezone.now(),
            rssi_data=request['data'],
        )
    elif request['data_type'] == SNR_DATA:
        item.update(
            update_time=timezone.now(),
            snr_data=request['data'],
        )
    elif request['data_type'] == BATTERY_DATA:
        item.update(
            update_time=timezone.now(),
            battery_data=request['data'],
        )

    response["status"] = "success"
    cmd = str(ManholeData.objects.get(address=request['address']).command)
    if cmd != '0':
        response["status"] = "cmd"
        response[request['address']] = cmd
        ManholeData.objects.filter(address=request['address']).update(command="0")

    return HttpResponse(json.dumps(response), content_type="application/json")


def post_billboard(req):
    response = {}
    if req.method == 'GET':
        data = {}
        data["x"] = str(req.GET.get("x"))
        data["y"] = str(req.GET.get("y"))
        data["node_id"] = str(req.GET.get("node_id"))
    elif req.method == 'POST':
        data = {}
        data["x"] = str(req.POST.get("x"))
        data["y"] = str(req.POST.get("y"))
        data["node_id"] = str(req.POST.get("node_id"))
        response = {}

    if data["x"] == "None" or data["y"]== "None":
        response["err"] = "wrong dataformat"
        return HttpResponse(json.dumps(response), content_type="application/json")

    item = BillBoardData.objects.filter(nodeid=data["node_id"])
    if not item:
        response["err"] = "%s is not in database" % data["node_id"]
        return HttpResponse(json.dumps(response), content_type="application/json")
    item.update(
        update_time=timezone.now(),
        x=data["x"],
        y=data["y"],
    )
    response["status"] = "success"
    return HttpResponse(json.dumps(response), content_type="application/json")
