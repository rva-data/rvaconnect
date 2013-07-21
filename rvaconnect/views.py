from django.shortcuts import render
from events.models import Event
from places.models import Place


def index(request):
    """
    """
    place = Place.active.all()[0]
    events_list = Event.current.all()[:3]
    return render(request, "index.html",
            {'events_list': events_list, 'place': place})
