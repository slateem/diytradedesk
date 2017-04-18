from django.conf.urls import url, include

from diy_dashboard import views

urlpatterns = [
	url(r'^$', views.index, name="dashboard"),
	url(r'^trade/create/$', views.trade_create, name="trade_create"),
	url(r'^trade/(?P<pk>[-\w+]+)/edit/$', views.trade_edit, name="trade_edit"),
	url(r'^trade/(?P<pk>[-\w+]+)/delete/$', views.trade_delete, name="trade_delete"),
	url(r'^trade/(?P<pk>[-\w+]+)/$', views.trade_detail, name="trade_detail"),
]