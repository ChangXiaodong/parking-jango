import urllib
import urllib2
import json
import subprocess
import pexpect
import time
import datetime

url = "http://121.42.213.241"
# url = "http://127.0.0.1:8000"
with open("/home/pi/manhole/configure/config.conf", "r") as f:
    conf = json.loads(f.readline())
relay_id = conf["relay_id"]
data = {}
data["relay_id"] = relay_id
post_data = urllib.urlencode(data)
feedback = "Net err"
local_port = ""
remote_port = ""
print("wait for net ready")
time.sleep(10)
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

subprocess.Popen(["sudo", "python", "/home/pi/manhole/monitor.py"])
status = ""
if local_port:
    for i in range(5):
        try:
            tunnel_command = 'ssh -NR {}:localhost:22 cxd@121.42.213.241'.format(local_port)
            ssh_tunnel = pexpect.spawn(tunnel_command)
            ssh_tunnel.expect('password:')
            time.sleep(1)
            ssh_tunnel.sendline("cxd\r")
            time.sleep(1)
            status = "success"
            break
        except:
            status = "failed"
            print(status)
else:
    status = "failed"

print("ssh tunnel finished:{}".format(status))

data = {"mobile": "18511693747", "tpl_id": "34037",
        "tpl_value": "#relayid#={}&#local_port#={}&#remote_port#={}&#status#={}".format(relay_id, local_port,
                                                                                        remote_port, status),
        "key": "cc0d7238ff63e5c51894fb505f2cbdbd"}
post_data = urllib.urlencode(data)
req = urllib2.Request(url='http://v.juhe.cn/sms/send?{}'.format(post_data))
res = urllib2.urlopen(req)
print("connection maintain")
while True:
    time.sleep(600)
    try:
        tunnel_command = 'ssh -NR {}:localhost:22 cxd@121.42.213.241'.format(local_port)
        ssh_tunnel = pexpect.spawn(tunnel_command)
        ssh_tunnel.expect('password:')
        time.sleep(1)
        ssh_tunnel.sendline("cxd\r")
        time.sleep(1)
        status = "ssh success"
    except:
        status = "ssh failed"
        print(status)
