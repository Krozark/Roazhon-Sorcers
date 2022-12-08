# -*- coding: utf-8 -*-
from django.urls import include, path, re_path
from website.views import ArticleListView, ArticleDetailView, contactView


urlpatterns = [
    path('', ArticleListView.as_view(), name="website-home"),
    re_path(r'^post/(?P<pk>[0-9]+)$', ArticleDetailView.as_view(), name="website-article"),
    path('contact', contactView, name="website-contact"),
]
