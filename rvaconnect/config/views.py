from django.shortcuts import render
from events.models import Event
from places.models import FeaturedPlace


def index(request):
    """
    Renders the index page, the primary landing page.
    """
    place = FeaturedPlace.objects.featured()
    events_list = Event.current.all()[:3]
    return render(request, "index.html",
            {'events_list': events_list, 'place': place})
