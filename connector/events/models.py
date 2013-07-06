import markdown

from datetime import datetime

from django.db import models
from model_utils.models import TimeStampedModel, TimeFramedModel


class ActiveManager(models.Manager):
    """
    Manager class for returning only active events.

    This functionality ensures that events can be removed from the public site
    without needing to be deleted from the database. This manager should be
    used for detail views, as even past events should be shown.
    """
    def get_query_set(self):
        return super(ActiveManager, self).get_queryset().filter(is_active=True)


class CurrentManager(ActiveManager):
    """
    Manager class for returning events which have yet to occur.

    This functionality should be used for list views and/or search indexing.
    """
    def get_query_set(self):
        return super(CurrentManager, self).get_queryset().filter(end__lte=datetime.now)


class Event(TimeStampedModel, TimeFramedModel):
    """
    Basic model for listing events.
    """
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
    notes = models.TextField(blank=True, null=True,
            help_text="Optional notes that will not be displayed publicly")

    objects = models.Manager()
    active = ActiveManager()
    current = CurrentManager()

    class Meta:
        ordering = ['start']

    def __unicode__(self):
        return self.name

    def save(self, *args, **kwargs):
        self.description = markdown.markdown(self.description_markdown,
                output_format='html5')
        return super(Event, self).save(*args, **kwargs)
