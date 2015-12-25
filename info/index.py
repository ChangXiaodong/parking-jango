from django.shortcuts import render, render_to_response, RequestContext
from django.http import HttpResponse
from info.models import ParkData, ParkDataHistory

def index(req):
    return render_to_response('info/index.html')



