from django.conf.urls import url

from info import views

urlpatterns = [
    url(r'^$', views.index, name='showinfo'),
]
