__author__ = 'Changxiaodong'
import urllib
import urllib2
data = {}
data["relay_id"] = "0086-110108-00022105-01"
data["data"]=""
num = 254
for i in range(14,20):
	data["data"] = data["data"] + "0086-110108-00022105-" + str(i).zfill(4) + "|" + str(num) + ','

databuf=""
databuf = data["data"]
data["data"] = databuf[:-1]
data["park_id"] = "22105"
post_data = urllib.urlencode(data)
try:
	response = urllib2.urlopen("http://127.0.0.1:8000/info/post/", post_data)
	print response.read()
except urllib2.HTTPError,error:
	print "ERROR: ",error