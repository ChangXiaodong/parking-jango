import urllib
import urllib2

data = {}
data["relay_id"] = "0001"
data["data"] = "132456"
data["area_id"] = "0001"
post_data = urllib.urlencode(data)
response = urllib2.urlopen("http://127.0.0.1:8000/database/post/", post_data)
feedback = response.read()
print(feedback)
