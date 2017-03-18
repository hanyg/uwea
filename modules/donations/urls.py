"""myproject URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.10/topics/http/urls/
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
from django.conf.urls import url
from django.contrib.auth.views import login, logout
from django.contrib import admin
import views

urlpatterns = [
    url(r'^accounts/login/$', login, name='login'),
    url(r'^accounts/logout/$', logout, name='logout', kwargs={'next_page': '/'}),
    url(r'^admin/', admin.site.urls),
    url(r'^$', views.donations, name='donations'),
    url(r'^envelope/(?P<pk>\d+)/$', views.envelope_detail, name='envelope_detail'),
    url(r'^envelope/new/$', views.envelope_new, name='envelope_new'),
    url(r'^envelope/(?P<pk>\d+)/edit/$', views.envelope_edit, name='envelope_edit'),
]
