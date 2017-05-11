# coding=utf-8
import platform
import serial
import time
import urllib
import urllib2
import json
import os
import datetime


class Monitor(object):
    def __init__(self, relay_id):
        if "Linux" in platform.system():
            self.url = "http://121.42.213.241"
        else:
            self.url = "http://127.0.0.1:8000"
        self.url = "http://121.42.213.241"
        self.relay_id = relay_id
        if not os.path.exists("./configure"):
            os.mkdir("./configure")
        self.log_path = "./log/log.txt"
        if not os.path.exists("./log"):
            os.mkdir("./log")

        serial_settings = {}
        if platform.system() == "Windows":
            serial_settings["port"] = "COM3"
            serial_settings["baudrate"] = "115200"
            serial_settings["stopbits"] = serial.STOPBITS_ONE
            serial_settings["parity"] = serial.PARITY_NONE
            # serial_settings["timeout"] = 0.01
        else:
            serial_settings["port"] = "/dev/ttyAMA0"
            serial_settings["baudrate"] = "115200"
            serial_settings["stopbits"] = serial.STOPBITS_ONE
            serial_settings["parity"] = serial.PARITY_NONE
            # serial_settings["timeout"] = 0.01

        self.uart = serial.Serial(**serial_settings)
        self.iptables = self.get_iptables()

        self.heart_beat_cnt = 0

        while not self.iptables:
            self.iptables = self.get_iptables()
            time.sleep(1)
            print("Net error")

        for v in self.iptables.values():
            self.channel = int(v[0])

        self.heart_beat_mask = 0

        self.FEATURE_BYTES = 13
        self.GET_ADDR_TYPE = 1
        self.DATA_START_TYPE = 2
        self.DATA_END_TYPE = 3
        self.WAKE_TYPE = 4
        self.PARAMS_SET_TYPE = 5
        self.OPEN_ALERT_TYPE = 6
        self.HEART_BEAT_TYPE = 7
        self.CLOSE_ALERT_TYPE = 8

    def get_active_node(self):
        data = {}
        data["relayid"] = self.relay_id
        post_data = urllib.urlencode(data)
        try:
            response = urllib2.urlopen("{}/database/active/".format(self.url), post_data)
            feedback = response.read()

        except urllib2.URLError:
            feedback = "Net err"
            print(feedback)
            return {"open": [], "close": []}
        active_node = eval(feedback)

        return active_node

    def save_log(self, msg):
        with open(self.log_path, "a+") as f:
            time_now = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
            f.write("{}: {} \n".format(time_now, msg))

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
        return iptables

    def lora_send(self, type, channel, addr, data=[]):
        channel = int(channel)
        addr = int(addr)
        type = int(type)

        int_data = map(int, data)
        self.uart.write(chr(addr >> 8))
        self.uart.write(chr(addr))
        self.uart.write(chr(channel))
        self.uart.write(chr(type))
        for v in int_data:
            self.uart.write(chr(v))
        self.uart.write(chr(0x0D))
        self.uart.write(chr(0x0A))

    def off_or_on_node(self):
        node = self.get_active_node()
        for sensor_id in node["close"]:
            for i in range(4):
                self.uart.timeout = 20
                self.uart.read(self.uart.inWaiting())
                addr = int(self.iptables[sensor_id][1])
                msg = "close({}):{},{}".format(i, self.channel, addr)
                print(msg)
                self.save_log(msg)
                self.lora_send(self.DATA_END_TYPE, self.channel, addr)
                time.sleep(1)
                self.lora_send(self.DATA_END_TYPE, self.channel, addr)

                recv = map(ord, self.uart.readline())
                if not recv:
                    continue
                if recv[0] != self.DATA_END_TYPE:
                    continue
                length = recv[1] << 8 | recv[2]
                msg = "receiving data, length:{}".format(length)
                print(msg)
                self.save_log(msg)
                self.uart.timeout = 20
                for i in range(length):
                    recv = map(ord, self.uart.read(self.FEATURE_BYTES))
                    if not recv:
                        msg = "{}/{} missed".format(i, length)
                        print(msg)
                        self.save_log(msg)
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
                    print("{}/{}: {}, {}, {}, {}, {}, {}, {},".format(
                        i, length,
                        start, end, index_len, width, peakvalue, other_peak, other_var
                    ))
                    post_data = urllib.urlencode(data)
                    urllib2.urlopen("{}/database/insert_data/".format(self.url), post_data)

                data = {"sensor_id": sensor_id, "status": "close"}
                post_data = urllib.urlencode(data)
                urllib2.urlopen("{}/database/node_status/".format(self.url), post_data)
                msg = "get data_finished"
                print(msg)
                self.save_log(msg)
                break
        for sensor in node["open"]:
            sensor_id = sensor.keys()[0]
            period = sensor.values()[0]
            period = min(period, 255)
            for i in range(3):
                self.uart.read(self.uart.inWaiting())
                self.channel = int(self.iptables[sensor_id][0])
                addr = int(self.iptables[sensor_id][1])
                msg = "open({}):{},{}".format(i, self.channel, addr)
                print(msg)
                self.save_log(msg)
                data_send = [period]
                self.lora_send(self.WAKE_TYPE, self.channel, addr, data_send)
                time.sleep(1)
                self.lora_send(self.WAKE_TYPE, self.channel, addr, data_send)
                self.uart.timeout = 10
                recv = map(ord, self.uart.readline())
                if recv and recv[0] == self.WAKE_TYPE:
                    data = {"sensor_id": sensor_id, "status": "open"}
                    post_data = urllib.urlencode(data)
                    urllib2.urlopen("{}/database/node_status/".format(self.url), post_data)
                    msg = "sensor: {} opened".format(sensor_id)
                    print(msg)
                    self.save_log(msg)
                    break

    def update_params(self):
        data = {"relayid": relay_id, "status": "update"}
        try:
            post_data = urllib.urlencode(data)
            response = urllib2.urlopen("{}/database/params/".format(self.url), post_data)
            feedback = eval(response.read())
        except:
            print("Net error")
            return []
        for sensor_id, params in feedback.items():
            for index, value in params.items():
                msg = "params set, sensor id:{} params:{} value:{}".format(sensor_id, index, value)
                print(msg)
                self.save_log(msg)
                for i in range(4):
                    self.uart.timeout = 10
                    addr = int(self.iptables[sensor_id][1])
                    msg = "send times:{} addr:{}".format(i, addr)
                    print(msg)
                    self.save_log(msg)
                    data_send = [index, (value >> 8) & 0xFF, value & 0xFF]
                    self.lora_send(self.PARAMS_SET_TYPE, self.channel, addr, data_send)
                    time.sleep(3)
                    self.lora_send(self.PARAMS_SET_TYPE, self.channel, addr, data_send)
                    recv = map(ord, self.uart.readline())
                    if not recv:
                        continue
                    type = recv[0]
                    recv_index = recv[1]
                    recv_value = recv[2] << 8 | recv[3]
                    msg = "recv index: {}  value: {}".format(recv_index, value)
                    print(msg)
                    self.save_log(msg)

                    if type == self.PARAMS_SET_TYPE and recv_index == int(index) and recv_value == int(value):
                        data = {"sensor_id": sensor_id, "index": index, "value": value, "status": "set"}
                        post_data = urllib.urlencode(data)
                        response = urllib2.urlopen("{}/database/params/".format(self.url), post_data)
                        msg = "params set status:{}".format(response.read())
                        print(msg)
                        self.save_log(msg)
                        break

    def recv_open_alert(self):
        if self.uart.inWaiting() != 0:
            recv = map(ord, self.uart.readline())
            if not recv:
                return
            type = recv[0]
            addr = recv[1]
            if type == self.OPEN_ALERT_TYPE:
                status = "open"
                msg = "open alert: {}".format(addr)
                print(msg)
                self.save_log(msg)
            elif type == self.CLOSE_ALERT_TYPE:
                status = "close"
                msg = "close alert: {}".format(addr)
                print(msg)
                self.save_log(msg)
            else:
                return

            sensor_id = "1"
            for key, value in self.iptables.items():
                if int(value[1]) == addr:
                    sensor_id = key
                    break
            data = {"sensor_id": sensor_id, "open_status": status}
            post_data = urllib.urlencode(data)
            response = urllib2.urlopen("{}/database/open_status/".format(self.url), post_data)
            msg = "open alert sensor_id: {}  open_status:{}  status:{}".format(sensor_id, status, response.read())
            print(msg)
            self.save_log(msg)

    def heart_beat(self):
        if datetime.datetime.now().minute % 48 != 0:
            self.heart_beat_mask = 0

        if self.heart_beat_mask == 0 and datetime.datetime.now().minute % 48 == 0:
            print(self.iptables.keys())
            print(self.heart_beat_cnt)
            self.heart_beat_mask = 1
            self.uart.timeout = 10
            sensor_id = self.iptables.keys()[self.heart_beat_cnt]
            msg = "send ({}) heart beat".format(sensor_id)
            print(msg)
            self.save_log(msg)
            self.heart_beat_cnt = (self.heart_beat_cnt + 1) % len(self.iptables.keys())
            addr = int(self.iptables[sensor_id][1])
            self.lora_send(self.HEART_BEAT_TYPE, self.channel, addr)
            recv = map(ord, self.uart.readline())
            if not recv:
                for i in range(3):
                    msg = "send times:{} addr:{}".format(i, addr)
                    print(msg)
                    self.save_log(msg)
                    self.lora_send(self.HEART_BEAT_TYPE, self.channel, addr)
                    time.sleep(1)
                    self.lora_send(self.HEART_BEAT_TYPE, self.channel, addr)
                    recv = map(ord, self.uart.readline())
                    if recv:
                        break

            if recv and recv[0] == self.HEART_BEAT_TYPE:
                battery = recv[1] << 8 | recv[2]
                data = {"sensor_id": sensor_id, "battery": battery}
                post_data = urllib.urlencode(data)
                response = urllib2.urlopen("{}/database/heart_beat/".format(self.url), post_data)
                msg = "heart beat status:{}".format(response.read())
                print(msg)
                self.save_log(msg)

    def run(self):
        while True:
            time.sleep(1)
            # 主机接收
            self.recv_open_alert()

            # 主机发送
            self.heart_beat()
            self.off_or_on_node()
            self.update_params()


if __name__ == "__main__":
    if "Linux" in platform.system():
        import RPi.GPIO as GPIO

        GPIO.setmode(GPIO.BOARD)
        GPIO.setup(12, GPIO.OUT)
        for i in range(3):
            GPIO.output(12, GPIO.HIGH)
            time.sleep(0.1)
            GPIO.output(12, GPIO.LOW)
            time.sleep(0.1)

    with open("./configure/config.conf", "r") as f:
        conf = json.loads(f.readline())
    relay_id = conf["relay_id"]
    monitor = Monitor(relay_id)
    monitor.run()
