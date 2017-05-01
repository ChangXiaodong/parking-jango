from django.conf.urls import url

from manhole_database import post_data

urlpatterns = [
    url(r'^post/', post_data.post_sensor_data, name='post_data'),
    url(r'^active/', post_data.active_node, name='active'),
    url(r'^iptables/', post_data.get_iptables, name='iptables'),
    url(r'^node_status/', post_data.node_status, name='node_status'),
    url(r'^insert_data/', post_data.insert_data, name='insert_data'),
]