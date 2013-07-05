from django.db import models
from model_utils import Choices
from model_utils.models import TimeStampedModel


class ActiveManager(models.Manager):
    """
    Manager class for returning only active places.
    """
    def get_query_set(self):
        return super().get_queryset().filter(is_active=True)


class Place(TimeStampedModel):
    """
    Basic model for listing places.
    """
    TYPES = Choices('co-working', 'coffee shop')

    name = models.CharField(max_length=100)
    description_markdown = models.TextField(default='')
    description = models.TextField(null=True)
    location = models.CharField(max_length=200, blank=True, null=True,
            help_text="This should be entered in a format amenable to geocoding.")
    url = models.URLField(blank=True, null=True)
    latitude = models.DecimalField(max_digits=10, decimal_places=7, null=True,
            blank=True)
    longitude = models.DecimalField(max_digits=10, decimal_places=7, null=True,
            blank=True)
    is_active = models.BooleanField(default=True)
    category = models.CharField(choices=TYPES, max_length=20)
    notes = models.TextField(blank=True, null=True,
            help_text="Optional notes that will not be displayed publicly")

    def __unicode__(self):
        return self.name
