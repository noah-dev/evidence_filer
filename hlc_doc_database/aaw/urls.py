from django.conf.urls import url
from . import views

app_name = 'aaw'
urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^upload/$', views.upload, name='index'),
    url(r'^taxonomy$', views.taxonomy, name='index'),
    url(r'^retrival$', views.retrival, name='index')
]
