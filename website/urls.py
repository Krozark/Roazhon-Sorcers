# -*- coding: utf-8 -*-
from django.conf.urls import include,url
from website.views import ArticleListView, ArticleDetailView, contactView


urlpatterns = [
    url(r'^$', ArticleListView.as_view(), name="website-home"),
    url(r'^post/(?P<pk>[0-9]+)$', ArticleDetailView.as_view(), name="website-article"),
    url(r'^contact$', contactView, name="website-contact"),    
]
