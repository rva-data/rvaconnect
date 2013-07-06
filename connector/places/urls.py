from django.conf.urls import patterns, url

from .views import PlaceList, PlaceDetail


urlpatterns = patterns('',
    url(r'^$', view=PlaceList.as_view(), name="place_list"),
    url(r'^(?P<pk>\d+)/$', view=PlaceDetail.as_view(), name="place_detail"),
)
