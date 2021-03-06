# from django.urls import path
#
# from . import views
#
# urlpatterns = [
#     path('^$', views.index, name='index'),
# ]
from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^(?P<room_name>[^/]+)/$', views.room, name='room'),
]
