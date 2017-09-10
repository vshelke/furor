from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^del/(?P<id>[0-9]+)/$', views.delete, name='delete'),
    url(r'^tag/(?P<tag>[a-z]+)/$', views.tag, name='teg'),


]
