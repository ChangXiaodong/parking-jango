import pexpect
import time

print("run")
tunnel_command = '/usr/bin/ssh -NR 20006:localhost:22 cxd@121.42.213.241'
ssh_tunnel = pexpect.spawn(tunnel_command)
ssh_tunnel.interact()
print("finished")
while True:
    time.sleep(10)