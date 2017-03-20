from django.conf.urls import url, include
from django.contrib.auth.views import login, logout
from django.contrib import admin
import views

urlpatterns = [
    url(r'^accounts/login/$', login, name='login'),
    url(r'^accounts/logout/$', logout, name='logout', kwargs={'next_page': '/'}),
    url(r'^admin/', admin.site.urls),
    url(r'^$', views.main, name='main'),
    url(r'^donations/', include('donations.urls')),
]
