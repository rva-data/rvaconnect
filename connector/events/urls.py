from django.conf.urls import patterns, url

from .views import EventList, EventDetail


urlpatterns = patterns('',
    url(r'^$', view=EventList.as_view(), name="event_list"),
    url(r'^(?P<pk>\d+)/$', view=EventDetail.as_view(), name="event_detail"),
)
