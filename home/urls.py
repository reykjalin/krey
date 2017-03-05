from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^login/$', views.loginView, name='Login'),
    url(r'^logout/$', views.logoutView, name='Logout'),
    url(r'^$', views.index, name='Home'),
]
