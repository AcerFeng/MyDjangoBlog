from django.conf.urls import url, include

from . import views

urlpatterns = [
    url(r'^index/$', views.index),
    url(r'^article/(?P<article_id>[0-9]+)$', views.article_page, name='article_page'),
    url(r'^edit_article/(?P<article_id>[0-9]+)?$', views.edit_article, name='edit'),
    url(r'^edit_action/$', views.edit_action, name='edit_action'),
]