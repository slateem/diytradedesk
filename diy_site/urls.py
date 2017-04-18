from django.conf.urls import url, include

from diy_site import views

urlpatterns = [
	url(r'^$', views.index, name='index'),
]