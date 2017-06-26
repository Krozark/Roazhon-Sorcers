# -*- coding: utf-8 -*-
from django.conf.urls import include,url
from website.views import HomeView, ArticleDetailView


urlpatterns = [
    url(r'^$', HomeView.as_view(), name="website-home"),
    url(r'^post/(?P<pk>[0-9]+)$', ArticleDetailView.as_view(), name="website-article"),
]
