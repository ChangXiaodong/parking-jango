from django.shortcuts import render, render_to_response, RequestContext
from django.http import HttpResponse
from info.models import ParkData, ParkDataHistory
from django.utils import timezone
import urllib
import urllib2

def index(req):
    if req.method == 'POST':
        parkdata = {}
        post_data = ""
        dataandid = str(req.POST.get("data")).split(",")
        for item in dataandid:
            parkdata["node_id"] = item.split("|")[0]
            parkdata["data"] = item.split("|")[1]
            parkdata["relay_id"] = str(req.POST.get("relay_id"))
            parkdata["park_id"] = str(req.POST.get("park_id"))
            # for i in range(1,51):
            #     ParkData.objects .create(time=datetime.datetime.now(),relayid="0086-110108-00022105-01", data="0", parkid="22105", nodeid="0086-110108-00022105-" + str(i).zfill(4))
            ParkDataHistory.objects.create(
                    time=timezone.now(),
                    relayid=parkdata["relay_id"],
                    data=parkdata["data"],
                    parkid=parkdata["park_id"],
                    nodeid=parkdata["node_id"]
            )
            ParkData.objects .filter(nodeid=parkdata["node_id"]).update(
                    time=timezone.now(),
                    relayid=parkdata["relay_id"],
                    data=parkdata["data"],
                    parkid=parkdata["park_id"]
            )
            if parkdata["data"] == '0' or parkdata["data"] == '1':
                post_data += parkdata["node_id"] + "|" + parkdata["data"] + ","

        if post_data:
            parkdata["data"] = post_data[:-1]
        print dataandid
        try:
            response = urllib2.urlopen("http://123.57.37.66:8080/sensor/post/status", urllib.urlencode(parkdata), timeout=1)
            return HttpResponse("Success")
        except urllib2.HTTPError,err:
            return HttpResponse(err)


    else:
        return render_to_response('info/infoindex.html',{'parkdata':"GET"})

