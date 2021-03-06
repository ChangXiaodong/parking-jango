from django.conf.urls import url

from manhole_database import post_data

urlpatterns = [
    url(r'^post/', post_data.post_sensor_data, name='post_data'),
    url(r'^active/', post_data.active_node, name='active'),
    url(r'^iptables/', post_data.get_iptables, name='iptables'),
    url(r'^node_status/', post_data.node_status, name='node_status'),
    url(r'^insert_data/', post_data.insert_data, name='insert_data'),
    url(r'^params/', post_data.params_set, name='params'),
    url(r'^open_status/', post_data.open_status, name='open_status'),
    url(r'^heart_beat/', post_data.heart_beat, name='heart_beat'),
    url(r'^relay_start/', post_data.relay_start, name='relay_start'),
    url(r'^query/', post_data.query, name='query'),
    url(r'^ssh/', post_data.auto_ssh, name='ssh'),
    url(r'^post_level/', post_data.post_level, name='level'),
]
