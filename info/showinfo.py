from django.shortcuts import render, render_to_response, RequestContext
from django.http import HttpResponse
from info.models import ParkData, ParkDataHistory

def info(req):
    datastruct = []

    for i in range(1,28):
        item = ParkData.objects.get(nodeid="0086-110108-00022105-"+str(i).zfill(4))
        datastruct.append([(str(item.time.strftime('%Y-%m-%d %H:%M:%S'))),
                     str(i).zfill(2),
                     str(item.data),
                     str(item.command)])
    return render_to_response('info/infoindex.html',{'datastruct':datastruct})
	
def cmd(req):
    datastruct = []

    for i in range(1,28):
        item = ParkData.objects.get(nodeid="0086-110108-00022105-"+str(i).zfill(4))
        datastruct.append([(str(item.time.strftime('%Y-%m-%d %H:%M:%S'))),
                     str(i).zfill(2),
                     str(item.data),
                     str(item.command)])
    return render_to_response('info/cmdindex.html',{'datastruct':datastruct})



