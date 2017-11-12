from django.conf.urls import url
from . import views

app_name = 'api'
urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^upload/$', views.upload, name='upload'),
    url(r'^retrival/$', views.retrival, name='retrival'),
    url(r'^serve/$', views.serve_file, name='serve')
]
