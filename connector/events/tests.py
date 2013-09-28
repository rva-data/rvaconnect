from django.test import TestCase
from django.core.urlresolvers import reverse

from .models import Event


class ViewTests(TestCase):

    def test_ical_format(self):
        """Ensure that iCal format is returned"""
        response = self.client.get((reverse('event_list_ical')))
        self.assertEqual(response['Content-Type'],
                'text/calendar; charset=utf8')


class ModelTests(TestCase):

    def test_event_uid(self):
        """Ensure the UID is created"""
        e = Event(name="Test")
        self.assertFalse(getattr(e, 'uid'))
        e.save()
        self.assertTrue(e.uid)


class FeedTests(TestCase):
    pass
