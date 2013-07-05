from django.contrib import admin

from .models import Event
from .forms import EventAdminForm


class EventAdmin(admin.ModelAdmin):
    form = EventAdminForm


admin.site.register(Event, EventAdmin)
