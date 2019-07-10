from django.conf.urls import url, include
from . import views

urlpatterns = [
	url(r'^$',views.indexView, name='index'), #index
    url(r'^Historia/(?P<historia_id>[0-9]+)$', views.historiaView),
    url(r'^Tecnica/(?P<tecnica_id>[0-9]+)$', views.tecnicaView),
    url(r'^search/', include('haystack.urls')),
]
