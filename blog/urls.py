from django.conf.urls import url
from . import views

urlpatterns = [
	# /blog/ 
    url(r'^$', views.index, name='index'),
    # /blog/{id}
    url(r'^(?P<blog_id>[0-9]+)/$', views.detail, name='detail'),
]