import urllib
import urllib2
import json
import os
import datetime


def update_iptables(relay_id):
    path = "./configure/iptables_{}.conf".format(relay_id)
    log = "./log/log.txt"
    if not os.path.exists("./configure"):
        os.mkdir("./configure")
    if not os.path.exists("./log"):
        os.mkdir("./log")

    data = {}
    data["relayid"] = relay_id
    post_data = urllib.urlencode(data)
    try:
        response = urllib2.urlopen("http://127.0.0.1:8000/database/iptable/", post_data)
        feedback = response.read()
    except urllib2.URLError:
        feedback = "Net err"

    if feedback == "Net err":
        with open(log, "a+") as f:
            time = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
            f.write("{}:Net err\n".format(time))
        return "Net err"

    print(feedback)


    if os.path.exists(path):
        with open(path, "r") as f:
            exist_iptables = json.loads(f.readline())
        new_iptables = json.loads(feedback)
        for sensor_id, [channel, net_address] in new_iptables.items():
            exist_iptables[sensor_id] = [channel, net_address]
        with open(path, "w") as f:
            f.write(json.dumps(exist_iptables))
    else:
        with open(path, "w") as f:
            f.write((feedback))
    with open(log, "a+") as f:
        time = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        f.write("{}:update iptables\n".format(time))

def get_iptables(relay_id, sensor_id):
    path = "./configure/iptables_{}.conf".format(relay_id)
    if os.path.exists(path):
        with open(path, "r") as f:
            exist_iptables = json.loads(f.readline())
        if exist_iptables.get(str(sensor_id), "Null") != "Null":
            return exist_iptables[str(sensor_id)]
        else:
            update_iptables(relay_id)
            with open(path, "r") as f:
                exist_iptables = json.loads(f.readline())
            if exist_iptables.get(str(sensor_id), "Null") != "Null":
                return exist_iptables[str(sensor_id)]
            else:
                return "sensor_id doesn't exist in database!"
    else:
        update_iptables(relay_id)
        if not os.path.exists(path):
            return "Net err"
        else:
            return get_iptables(relay_id, sensor_id)




if __name__ == "__main__":
    update_iptables(1)
