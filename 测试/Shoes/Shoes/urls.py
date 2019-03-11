from django.conf.urls import url
from .views import *
urlpatterns = [
    url(r'^getusershoes/(\d*)$',getusershoes_views),
    url(r'^updateusershoes/$',updateusershoes_views),
]