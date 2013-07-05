from django.contrib import admin

from .models import Place
from .forms import PlaceAdminForm


class PlaceAdmin(admin.ModelAdmin):
    form = PlaceAdminForm


admin.site.register(Place, PlaceAdmin)
