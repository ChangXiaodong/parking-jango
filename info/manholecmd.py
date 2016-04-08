from django.shortcuts import render, render_to_response, RequestContext
from django.http import HttpResponse,HttpResponseRedirect
from info.models import ManholeData, ManholeDataHistory


def cmd_manhole(req):
    nodeid = req.GET.get("num")
    cmd = req.GET.get("cmd")
    ManholeData.objects.filter(nodeid=nodeid).update(
            command=cmd
        )
    return HttpResponseRedirect("/info/manhole-config/?id="+nodeid)



