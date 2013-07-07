from django.views.generic import DetailView, ListView

from .models import Place


class PlaceDetail(DetailView):
    """
    A detail view for places which should fetch the place based on the passed
    ID.
    """
    queryset = Place.active.all()
    template_name = "places/place_detail.html"
    context_object_name = "place"


class PlaceList(ListView):
    """
    A list view for places.
    """
    queryset = Place.active.all()
    template_name = "places/place_list.html"
    context_object_name = "places_list"

    def get_context_data(self, **kwargs):
        context = super(PlaceList, self).get_context_data(**kwargs)
        context.update({'geocoded_places': Place.active.geocoded()})
        return context
