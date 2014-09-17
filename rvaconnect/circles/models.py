import markdown

from django.db import models
from model_utils.models import TimeStampedModel
from model_utils.fields import StatusField
from model_utils import Choices


class ActiveManager(models.Manager):
    """
    Manager class for returning only active events.

    This functionality ensures that events can be removed from the public site
    without needing to be deleted from the database. This manager should be
    used for detail views, as even past events should be shown.
    """
    def get_queryset(self):
        return super(ActiveManager, self).get_queryset().filter(is_active=True)


class Group(TimeStampedModel):
    """
    Model for managing groups like meetups, associations, etc.
    """
    STATUS = Choices('active', 'inactive', 'defunct')

    name = models.CharField(max_length=100)
    slug = models.SlugField(max_length=100,
            help_text="This is a field of just lowercase letters, numbers, and dashes used in the URL")
    description_markdown = models.TextField(default='')
    description = models.TextField(null=True)
    status = StatusField(choices_name='STATUS')
    url = models.URLField(blank=True, null=True)
    is_active = models.BooleanField(default=True)
    notes = models.TextField(blank=True, null=True,
            help_text="Optional notes that will not be displayed publicly")

    objects = models.Manager()
    active = ActiveManager()

    class Meta:
        ordering = ['name']
        verbose_name = 'group'
        verbose_name_plural = 'groups'

    def __unicode__(self):
        return self.name

    def save(self, *args, **kwargs):
        self.description = markdown.markdown(self.description_markdown,
                output_format='html5')
        return super(Group, self).save(*args, **kwargs)
