from django.conf.urls import url

from info import views
from info import showinfo
from info import index
urlpatterns = [
    url(r'^$', index.index, name='index'),
    url(r'^post/', views.index, name='showinfo'),
    url(r'^show/', showinfo.index, name='info'),
]
