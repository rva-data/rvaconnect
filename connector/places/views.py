from django.views.generic import DetailView, ListView

from .models import Place


class PlaceDetail(DetailView):
    """
    A detail view for places which should fetch the place based on the passed
    ID.
    """
    model = Place
    template_name = "places/place_detail.html"
    context_object_name = "place"


class PlaceList(ListView):
    """
    A list view for places.
    """
    queryset = Place.active.all()
    template_name = "places/place_list.html"
    context_object_name = "place_list"
