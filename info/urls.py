from django.conf.urls import url

from info import views
from info import showinfo

urlpatterns = [
    url(r'^post/', views.index, name='showinfo'),
    url(r'^show/', showinfo.index, name='info'),
]
