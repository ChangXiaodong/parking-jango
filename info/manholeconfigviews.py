from django.shortcuts import render, render_to_response, RequestContext
from django.http import HttpResponse, HttpResponseRedirect
from info.models import ManholeData, ManholeDataHistory
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
    address = int(req.GET.get("id"))
    try:
        item = ManholeData.objects.get(address=address)
    except ManholeData.DoesNotExist, err:
        return render_to_response('info/homepage/manholeconfig.html')
    datadic = {}
    datadic['address'] = address
    datadic['TMR_data'] = int(item.TMR_data)
    datadic['reed_data'] = int(item.reed_data)
    datadic['rssi_data'] = int(item.rssi_data)
    datadic['snr_data'] = int(item.snr_data)
    datadic['battery_data'] = int(item.battery_data)
    datadic['threshold'] = int(item.threshold)
    datadic['time'] = str(item.update_time.strftime('%Y-%m-%d %H:%M:%S'))
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
