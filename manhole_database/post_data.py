# coding=utf-8
from django.http import HttpResponse
from manhole_database.models import Data
import json


def post_sensor_data(req):
    if req.method == 'POST':
        # dataandid = req.POST.get("data")
        print("received")
        print(req.POST)
        return HttpResponse(json.dumps(req.POST), content_type="application/json")
    if req.method == 'GET':
        return HttpResponse(json.dumps(req.GET), content_type="application/json")
