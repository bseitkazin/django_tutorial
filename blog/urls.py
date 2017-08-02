from django.conf.urls import url
from . import views

app_name = 'blog'

urlpatterns = [
	# /blog/ 
    url(r'^$', views.index, name='index'),
    # /blog/{blog_id}
    url(r'^(?P<blog_id>[0-9]+)/$', views.detail, name='detail'),
    # /blog/{blog_id}/favorite/
    url(r'^(?P<blog_id>[0-9]+)/favorite/$', views.favorite, name='favorite'),
]