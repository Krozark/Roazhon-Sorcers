# -*- coding: utf-8 -*-
#from django.conf import settings
from django.conf.urls import include,url
#from website.views import TestView
#from website.models import *
from django.views.generic import TemplateView


urlpatterns = [
    url(r'', TemplateView.as_view(template_name="website/home.html")),
]
