from django.conf.urls import url
from . import views

app_name = 'aaw'
urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^upload/$', views.upload, name='upload'),
    url(r'^taxonomy/$', views.taxonomy, name='taxonomy'),
    url(r'^retrival/$', views.retrival, name='retrival')
]
