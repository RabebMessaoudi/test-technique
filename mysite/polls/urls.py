from django.conf.urls import url
from . import views


app_name = 'polls'

urlpatterns = [

    # /Equipe/
    url(r'^$', views.index, name='index'),

    # /Equipe/712
    url(r'^(?P<id>[0-9]+)/$', views.detail, name='detail'),


]