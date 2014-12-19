import markdown

from django.db import models
from django.core.urlresolvers import reverse
from model_utils import Choices
from model_utils.models import TimeStampedModel


class ActiveManager(models.Manager):
    """
    Manager class for returning only active places.
    """
    def get_queryset(self):
        return super(ActiveManager, self).get_queryset().filter(is_active=True)

    def geocoded(self):
        """
        Returns a queryset of places which have both a latitude and longitude
        associated with them.
        """
        return self.get_queryset().filter(latitude__isnull=False,
                longitude__isnull=False)


class FeaturedManager(models.Manager):

    def featured(self):
        try:
            return super(FeaturedManager, self).get_queryset()[0].place
        except IndexError:
            return None


class Place(TimeStampedModel):
    """
    Basic model for listing places.
    """
    TYPES = Choices('co-working', 'coffee shop')

    name = models.CharField(max_length=100)
    slug = models.SlugField(max_length=100,
            help_text="This is a field of just lowercase letters, numbers, and dashes used in the URL")
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

    objects = models.Manager()
    active = ActiveManager()

    def __str__(self):
        return self.name

    def save(self, *args, **kwargs):
        self.description = markdown.markdown(self.description_markdown,
                output_format='html5')
        return super(Place, self).save(*args, **kwargs)

    def get_absolute_url(self):
        return reverse('place_detail', kwargs={'slug': self.slug, 'pk': self.pk})

    @property
    def geolocation(self):
        """
        Returns the geolocation in GIS Point format (longitude, latitude)
        """
        if self.latitude and self.longitude:
            return self.longitude, self.latitude


class FeaturedPlace(TimeStampedModel):
    place = models.ForeignKey(Place, related_name="featured_links")

    objects = FeaturedManager()

    class Meta:
        ordering = ['-created']

    def __str__(self):
        return "{0}: {1}".format(self.place.name, self.created.date())
