from django.shortcuts import render, render_to_response, RequestContext
from django.http import HttpResponse
from info.models import ParkData
from info.models import ManholeData
from info.models import BillBoardData
from django.utils import timezone


def creatparking(req):
    for i in range(1, 28):
        ParkData.objects.create(
            time=timezone.now(),
            changed_time=timezone.now(),
            relayid="0086-110108-00022105-01",
            data="0",
            parkid="22105",
            nodeid="0086-110108-00022105-" + str(i).zfill(4),
            command="0"
        )
    return HttpResponse('creat parking finish')

def creatmanhole(req):
    manholedata = {}
    for i in range(1, 10):
        ManholeData.objects.create(
            update_time=timezone.now(),
            changed_time=timezone.now(),
            areaid="0",
            address=i,
            command="0",
            TMR_data="0",
            threshold="0",
            reed_data = "0",
            rssi_data = "0",
            snr_data = "0",
            battery_data = "0",
            last_disable_time = '2016-04-07 10:58:41',
            administrator = 'xiaoxiami',
            remarks = ''
        )
    return HttpResponse('creat manhole finish')

def creat_billboard(req):
    for i in range(1, 11):
        BillBoardData.objects.create(
            update_time=timezone.now(),
            nodeid=str(i).zfill(4),
            data="0",
        )
    return HttpResponse('creat Billboard finish')
