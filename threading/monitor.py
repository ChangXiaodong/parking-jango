import platform
import serial
import threading
import time
import urllib
import urllib2
import json
import os
import datetime


class Monitor(object):
    def __init__(self, relay_id):
        self.url = "http://127.0.0.1:8000"
        self.relay_id = relay_id
        if not os.path.exists("./configure"):
            os.mkdir("./configure")
        self.log_path = "./log/log.txt"

        serial_settings = {}
        if platform.system() == "Windows":
            serial_settings["port"] = "COM3"
            serial_settings["baudrate"] = "115200"
            serial_settings["stopbits"] = serial.STOPBITS_ONE
            serial_settings["parity"] = serial.PARITY_NONE
            # serial_settings["timeout"] = 0.01
        else:
            serial_settings["stopbits"] = serial.STOPBITS_ONE
            serial_settings["parity"] = serial.PARITY_NONE
            # serial_settings["timeout"] = 0.01
        self.uart = serial.Serial(**serial_settings)
        self.iptables = self.get_iptables()

        self.FEATURE_BYTES = 13
        self.GET_ADDR_TYPE = 1
        self.DATA_START_TYPE = 2
        self.DATA_END_TYPE = 3
        self.WAKE_TYPE = 4

    def get_active_node(self):
        data = {}
        data["relayid"] = self.relay_id
        post_data = urllib.urlencode(data)
        try:
            response = urllib2.urlopen("{}/database/active/".format(self.url), post_data)
            feedback = response.read()
        except urllib2.URLError:
            feedback = "Net err"
        active_node = eval(feedback)

        return active_node

    def get_iptables(self):
        data = {}
        data["relayid"] = self.relay_id
        post_data = urllib.urlencode(data)
        try:
            response = urllib2.urlopen("{}/database/iptables/".format(self.url), post_data)
            feedback = response.read()
            iptables = eval(feedback)
        except urllib2.URLError:
            iptables = []
        print(iptables)
        with open(self.log_path, "a+") as f:
            f.write("iptables:{}\n".format(iptables))
        return iptables

    def send_wakeup(self, channel, addr):
        self.uart.write(chr(addr >> 8).encode("ISO-8859-1"))
        self.uart.write(chr(addr).encode("ISO-8859-1"))
        self.uart.write(chr(channel).encode("ISO-8859-1"))
        self.uart.write(chr(self.WAKE_TYPE).encode("ISO-8859-1"))
        self.uart.write(chr(0x0D).encode("ISO-8859-1"))
        self.uart.write(chr(0x0A).encode("ISO-8859-1"))

    def send_getdata_then_sleep(self, channel, addr):
        self.uart.write(chr(addr >> 8).encode("ISO-8859-1"))
        self.uart.write(chr(addr).encode("ISO-8859-1"))
        self.uart.write(chr(channel).encode("ISO-8859-1"))
        self.uart.write(chr(self.DATA_END_TYPE).encode("ISO-8859-1"))
        self.uart.write(chr(0x0D).encode("ISO-8859-1"))
        self.uart.write(chr(0x0A).encode("ISO-8859-1"))

    def run(self):
        print("keep alive\n")
        while True:
            time.sleep(1)
            node = self.get_active_node()
            for sensor_id in node["close"]:
                for i in range(4):
                    self.uart.timeout = 10
                    channel = int(self.iptables[sensor_id][0])
                    addr = int(self.iptables[sensor_id][1])
                    print("close({}):{},{}".format(i, channel, addr))
                    self.send_getdata_then_sleep(channel, addr)
                    recv = map(ord, self.uart.readline())
                    if not recv:
                        if i == 1:
                            self.send_getdata_then_sleep(channel, addr)
                            time.sleep(1)
                        continue
                    length = recv[1] << 8 | recv[2]
                    print("receiving data, length:{}".format(length))
                    self.uart.timeout = 200
                    for _ in range(length):
                        recv = map(ord, self.uart.read(self.FEATURE_BYTES))
                        if not recv:
                            continue
                        start = recv[0] << 8 | recv[1]
                        end = recv[2] << 8 | recv[3]
                        index_len = recv[4]
                        width = recv[5] << 8 | recv[6]
                        peakvalue = recv[7] << 8 | recv[8]
                        other_peak = recv[9] << 8 | recv[10]
                        other_var = recv[11] << 8 | recv[12]
                        data = {
                            "sensor_id": sensor_id,
                            "start_index": start,
                            "end_index": end,
                            "index_len": index_len,
                            "width": width,
                            "peakvalue": peakvalue,
                            "other_peak": other_peak,
                            "other_var": other_var
                        }
                        print(start, end, index_len, width, peakvalue, other_peak, other_var)
                        post_data = urllib.urlencode(data)
                        urllib2.urlopen("{}/database/insert_data/".format(self.url), post_data)

                    data = {"sensor_id": sensor_id, "status": "close"}
                    post_data = urllib.urlencode(data)
                    urllib2.urlopen("{}/database/node_status/".format(self.url), post_data)
                    print("get data_finished")
                    break

            for sensor_id in node["open"]:
                for i in range(3):
                    self.uart.timeout = 20
                    channel = int(self.iptables[sensor_id][0])
                    addr = int(self.iptables[sensor_id][1])
                    print("open({}):{},{}".format(i, channel, addr))
                    self.send_wakeup(channel, addr)
                    time.sleep(1)
                    self.send_wakeup(channel, addr)
                    recv = map(ord, self.uart.readline())
                    if recv and recv[0] == self.WAKE_TYPE:
                        data = {"sensor_id": sensor_id, "status": "open"}
                        post_data = urllib.urlencode(data)
                        urllib2.urlopen("{}/database/node_status/".format(self.url), post_data)
                        break


if __name__ == "__main__":
    relay_id = 1
    monitor = Monitor(relay_id)
    monitor.run()
