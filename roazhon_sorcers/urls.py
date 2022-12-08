"""roazhon_sorcers URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
import django
from django.urls import path, include, re_path
from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('comments/', include('django_comments.urls')),
    path('froala_editor/', include('froala_editor.urls')),
    path('hitcount/', include('hitcount.urls')),
    path('', include("website.urls")),
]

if settings.DEV:
    urlpatterns.append(re_path(r'^media/(.*)$', django.views.static.serve, {'document_root': settings.MEDIA_ROOT}))
