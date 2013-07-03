from django.contrib.gis.db import models
from model_utils import Choices
from model_utils.models import TimeStampedModel


class ActiveManager(models.Manager):
    """
    Manager class for returning only active places.
    """
    def get_query_set(self):
        return super().get_query_set().filter(is_active=True)


class Place(TimeStampedModel):
    """
    """
    TYPES = Choices('co-working', 'coffee shop')

    name = models.CharField(max_length=100)
    description = models.TextField()
    location = models.CharField(max_length=200, blank=True, null=True,
            help_text="This should be entered in a format amenable to geocoding.")
    url = models.URLField(blank=True, null=True)
    geolocation = models.PointField(null=True, blank=True)
    is_active = models.BooleanField(default=True)
    category = models.CharField(choices=TYPES, max_length=20)
