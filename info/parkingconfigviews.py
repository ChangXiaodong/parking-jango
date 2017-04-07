from django.shortcuts import render_to_response
from info.models import ParkData


def index(req):
    nodeid = "0086-110108-00022105-" + str(req.GET.get("id")).zfill(4)
    item = ParkData.objects.get(nodeid=nodeid)
    data = str(item.data)
    time = str(item.time.strftime('%Y-%m-%d %H:%M:%S'))
    datadic = {"nodeid": nodeid, "data": data, "time": time}
    return render_to_response('info/homepage/parkingconfig.html', {'datadic': datadic})
