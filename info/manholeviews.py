from django.shortcuts import render, render_to_response, RequestContext
from django.http import HttpResponse, HttpResponseRedirect
from info.models import ParkData, ParkDataHistory
from django.utils import timezone
import urllib
import urllib2
import json
import time
from manhole_database.models import Key
import linecache
import os


def index(req):
    # for i in range(1,51):
    #     ParkData.objects .create(time=timezone.now(),relayid="0086-110108-00022105-01", data="0", parkid="22105", nodeid="0086-110108-00022105-" + str(i).zfill(4))
    # return HttpResponse("Init Database")
    item = Key.objects.get(src="aliyun")
    times = item.query_times + 1
    Key.objects.filter(src="aliyun").update(query_times=times,time=timezone.now())
    log_path = "log/page_access_log.log"
    with open("log/page_access_log.log", "a+") as f:
        f.write("{}:REMOTE_IP->{}  USER_AGENT->{}\n".format(
            time.strftime('%Y-%m-%d  %H:%M:%S', time.localtime(time.time())),
            req.META["REMOTE_ADDR"],
            req.META["HTTP_USER_AGENT"],
        ))
    return render_to_response('info/homepage/manhole.html')

    # if req.method == 'POST':
    #     print 'views'
    #     parkdata = {}
    #     post_data = ""
    #     dataandid = str(req.POST.get("data")).split(",")
    #     cmdStack={}
    #
    #     for item in dataandid:
    #         parkdata["node_id"] = item.split("|")[0]
    #         parkdata["data"] = item.split("|")[1]
    #         parkdata["relay_id"] = str(req.POST.get("relay_id"))
    #         parkdata["park_id"] = str(req.POST.get("park_id"))
    #         ParkDataHistory.objects.create(
    #                 time=timezone.now(),
    #                 relayid=parkdata["relay_id"],
    #                 data=parkdata["data"],
    #                 parkid=parkdata["park_id"],
    #                 nodeid=parkdata["node_id"]
    #         )
    #         ParkData.objects .filter(nodeid=parkdata["node_id"]).update(
    #                 time=timezone.now(),
    #                 relayid=parkdata["relay_id"],
    #                 data=parkdata["data"],
    #                 parkid=parkdata["park_id"]
    #         )
    #         cmd = str(ParkData.objects .get(nodeid=parkdata["node_id"]).command)
    #
    #         if cmd != '0':
    #             cmdStack[parkdata["node_id"]] = cmd
    #             ParkData.objects.filter(nodeid=parkdata["node_id"]).update(command="0")
    #
    #
    #         if parkdata["data"] == '0' or parkdata["data"] == '1':
    #             post_data += parkdata["node_id"] + "|" + parkdata["data"] + ","
    #
    #
    #     if post_data:
    #         parkdata["data"] = post_data[:-1]
    #     try:
    #         response = urllib2.urlopen("http://123.57.37.66:8080/sensor/post/status", urllib.urlencode(parkdata), timeout=1)
    #         cmdStack["Status"] = "Success"
    #         return HttpResponse(json.dumps(cmdStack), content_type="application/json")
    #     except urllib2.HTTPError,err:
    #         return HttpResponse(err)
    # else:
    #     nodeid = req.GET.get("num")
    #     cmd = req.GET.get("cmd")
    #     with open("cmd_log.txt",'a+') as file:
    #         file.write(time.strftime('%Y-%m-%d  %H:%M:%S', time.localtime(time.time()))+"  "+nodeid+"  "+cmd+"\n")
    #     ParkData.objects .filter(nodeid=nodeid).update(
    #                 command=cmd
    #         )
    #     return HttpResponseRedirect('/info/cmd/')
