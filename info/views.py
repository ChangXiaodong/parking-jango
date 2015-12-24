from django.shortcuts import render
from django.http import HttpResponse

def index(req):
    return HttpResponse("Hello,xiaoxiami ,you are in park info")
# Create your views here.
