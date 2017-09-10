from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^cmp/(?P<id>[0-9]+)/(?P<option>[0-2]{1})/$', views.completed, name='completed'),
    url(r'^tag/(?P<tag>[a-z]+)/$', views.tag, name='tag'),
    url(r'^signup/$', views.signup, name='signup'),
    url(r'^login/$', views.u_login, name='u_login'),
    url(r'^logout/$', views.logout_view, name='logout_view'),
]
