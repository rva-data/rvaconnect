from datetime import datetime

from django.contrib.gis.db import models
from model_utils.models import TimeStampedModel, TimeFramedModel


class ActiveManager(models.Manager):
    """
    Manager class for returning only active events.

    This functionality ensures that events can be removed from the public site
    without needing to be deleted from the database. This manager should be
    used for detail views, as even past events should be shown.
    """
    def get_query_set(self):
        return super().get_query_set().filter(is_active=True)


class CurrentManager(ActiveManager):
    """
    Manager class for returning events which have yet to occur.

    This functionality should be used for list views and/or search indexing.
    """
    def get_query_set(self):
        return super().get_query_set().filter(end__lte=datetime.now)


class Event(TimeStampedModel, TimeFramedModel):
    """
    Basic model for listing events.
    """
    name = models.CharField(max_length=100)
    #start = models.DateTimeField()
    #end = models.DateTimeField()
    description = models.TextField()
    location = models.CharField(max_length=200, blank=True, null=True,
            help_text="This should be entered in a format amenable to geocoding.")
    url = models.URLField(blank=True, null=True)
    geolocation = models.PointField(null=True, blank=True)
    is_active = models.BooleanField(default=True)

    objects = models.Manager()
    active = ActiveManager()
    current = CurrentManager()
