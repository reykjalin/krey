from django.conf.urls import url
from . import views


urlpatterns = [
    url(r'^$', views.index, name='Torrents'),
    url(r'list$', views.list, name='TorrentList'),
    url(r'upload$', views.upload, name='TorrentUpload'),
]
