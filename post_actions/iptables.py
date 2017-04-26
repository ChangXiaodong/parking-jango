import urllib
import urllib2
import json
import os
import datetime

def update_iptables(relay_id):
    data = {}
    data["relayid"] = relay_id
    post_data = urllib.urlencode(data)
    response = urllib2.urlopen("http://127.0.0.1:8000/database/iptable/", post_data)
    feedback = response.read()

    print(feedback)
    path = "./configure/iptables.conf"
    log = "./log/log.txt"
    if os.path.exists(path):
        with open(path, "r") as f:
            exist_iptables = json.loads(f.readline())
        new_iptables = json.loads(feedback)
        for sensor_id, net_address in new_iptables.items():
            exist_iptables[sensor_id] = net_address
        with open(path, "w") as f:
            f.write(json.dumps(exist_iptables))
    else:
        with open(path, "w") as f:
            f.write((feedback))
    with open(log, "a+") as f:
        time = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        f.write("{}:update iptables\n".format(time))

if __name__ == "__main__":
    update_iptables(1)
