from django.conf.urls import url

from manhole_database import post_data

urlpatterns = [
    url(r'^post/', post_data.post_sensor_data, name='post_data'),
    url(r'^iptable/', post_data.get_iptables, name='iptable'),
]