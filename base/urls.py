from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^sponsors/', views.sponsors, name='sponsors'),
    url(r'^team/', views.team, name='team'),
]