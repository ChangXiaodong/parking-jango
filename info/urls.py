from django.conf.urls import url

from info import views
from info import showinfo
from info import index
from info import parkingviews
from info import manholeviews
from info import manholeconfigviews
from info import ajax
from info import manholecmd
urlpatterns = [
    url(r'^$', index.index, name='index'),
    url(r'^post/', views.index, name='showinfo'),
    url(r'^show/', showinfo.info, name='info'),
	url(r'^cmd/', showinfo.cmd, name='cmd'),
	url(r'^parking/', parkingviews.index),
	url(r'^manhole/', manholeviews.index),
	url(r'^ajax_parking/$', ajax.getParking, name='ajax-parking'),
	url(r'^ajax_manhole/$', ajax.getManhole, name='ajax-manhole'),
	url(r'^ajax_manholeitem/$', ajax.getManholeItem, name='ajax-manholeitem'),
	url(r'^manhole-post/', views.postmanhole, name='postmanhole'),
	url(r'^manhole-cmd/', ajax.cmd_manhole, name='cmd'),
	url(r'^manhole-config/', manholeconfigviews.index, name='manholeconfig'),
]
