__author__ = 'Changxiaodong'
import urllib
import urllib2
data = {}
data["relay_id"] = "0086-110108-00022105-01"
data["data"]=""
num = 0
for i in range(1,28):
	data["data"] = data["data"] + "0086-110108-00022105-" + str(i).zfill(4) + "|" + str(num) + ','

databuf=""
databuf = data["data"]
data["data"] = databuf[:-1]
data["park_id"] = "22105"
post_data = urllib.urlencode(data)
try:
	response = urllib2.urlopen("http://www.xiaoxiami.space/info/post/", post_data)
	feedback = eval(response.read())
except urllib2.HTTPError,error:
	print "ERROR: ",error

for key,value in feedback.items():
	if key!="Status":
		num = int(str(key).split("-")[-1])
		print num,value
		