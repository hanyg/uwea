from django.conf.urls import url
import views

urlpatterns = [
    url(r'^envelopes$', views.envelopes, name='envelopes'),
    url(r'^envelope/(?P<pk>\d+)/$', views.envelope_detail, name='envelope_detail'),
    url(r'^envelope/new/$', views.envelope_new, name='envelope_new'),
    url(r'^envelope/(?P<pk>\d+)/edit/$', views.envelope_edit, name='envelope_edit'),
    url(r'^campaigns$', views.campaigns, name='campaigns'),
    url(r'^campaign/(?P<pk>\d+)/$', views.campaign_detail, name='campaign_detail'),
    url(r'^campaign/new/$', views.campaign_new, name='campaign_new'),
    url(r'^campaign/(?P<pk>\d+)/edit/$', views.campaign_edit, name='campaign_edit'),
]
