from django.conf.urls import url

from info import views
from info import showinfo
from info import index
from info import parkingviews
from info import manholeviews
from info import manholeconfigviews
from info import ajax
from info import creatsql
from info import parkingconfigviews
from info import billboardviews

urlpatterns = [
    url(r'^$', index.index, name='index'),
    url(r'^post/', views.index, name='showinfo'),
    url(r'^show/', showinfo.info, name='info'),
    url(r'^cmd/', showinfo.cmd, name='cmd'),
    url(r'^creat-parking/', creatsql.creatparking, name='sql-parking'),
    url(r'^creat-manhole/', creatsql.creatmanhole, name='sql-manhole'),
    url(r'^creat-billboard/', creatsql.creat_billboard, name='sql-billboard'),
    url(r'^parking/', parkingviews.index),
    url(r'^manhole/', manholeviews.index),
    url(r'^ajax_parking/$', ajax.getParking, name='ajax-parking'),
    url(r'^ajax_manhole/$', ajax.getManhole, name='ajax-manhole'),
    url(r'^ajax_manholeitem/$', ajax.getManholeItem, name='ajax-manholeitem'),
    url(r'^ajax_parkingitem/$', ajax.getParkingItem, name='ajax-parkingitem'),
    url(r'^manhole-post/', views.postmanhole, name='postmanhole'),
    url(r'^manhole-cmd/', ajax.cmd_manhole, name='cmd'),
    url(r'^manhole-config/', manholeconfigviews.index, name='manholeconfig'),
    url(r'^manhole-update-threshold/', manholeconfigviews.update_threshold, name='threshold'),
    url(r'^parking-config/', parkingconfigviews.index, name='parkconfig'),

    url(r'^billboard-post/', views.post_billboard, name='postbillboard'),
    url(r'^billboard/', billboardviews.index),
    url(r'^ajax_billboard/$', ajax.getBillboard, name='ajax-billboard$'),
]
