import urllib
import urllib2
import json
import subprocess
import time

url = "http://121.42.213.241"
# url = "http://127.0.0.1:8000"
with open("./configure/config.conf", "r") as f:
    conf = json.loads(f.readline())
relay_id = conf["relay_id"]
data = {}
data["relay_id"] = relay_id
post_data = urllib.urlencode(data)
feedback = "Net err"
local_port = ""
remote_port = ""
for i in range(120):
    try:
        response = urllib2.urlopen("{}/database/relay_start/".format(url), post_data)
        feedback = response.read()
    except urllib2.URLError:
        feedback = "Net err"
        print(feedback)
    if feedback != "Net err":
        port = eval(feedback)
        print(port)
        local_port = port["local_port"]
        remote_port = port["remote_port"]
        break
    time.sleep(5)
if local_port:
    subprocess.Popen(["ssh", "-fCNR", "{}:localhost:22".format(local_port), "cxd@121.42.213.241"])
    status = "reverse ssh success"
else:
    status = "reverse ssh failed"

# data = {"mobile": "18511693747", "tpl_id": "34037",
#         "tpl_value": "#relayid#={}&#local_port#={}&#remote_port#={}&#status#={}".format(relay_id, local_port,
#                                                                                         remote_port, status),
#         "key": "cc0d7238ff63e5c51894fb505f2cbdbd"}
# post_data = urllib.urlencode(data)
# req = urllib2.Request(url='http://v.juhe.cn/sms/send?{}'.format(post_data))
# res = urllib2.urlopen(req)

subprocess.Popen(["sudo", "python", "monitor.py"])

print("finished")
