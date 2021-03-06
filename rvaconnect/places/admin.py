from django.contrib import admin

from .models import Place, FeaturedPlace
from .forms import PlaceAdminForm


class PlaceAdmin(admin.ModelAdmin):
    form = PlaceAdminForm
    prepopulated_fields = {"slug": ("name",)}


admin.site.register(Place, PlaceAdmin)
admin.site.register(FeaturedPlace)
