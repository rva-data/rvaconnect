from django.contrib import admin

from .forms import GroupAdminForm
from .models import Group


class GroupAdmin(admin.ModelAdmin):
    form = GroupAdminForm
    prepopulated_fields = {"slug": ("name",)}
    search_fields = ('name', 'description')
    list_filter = ('is_active',)


admin.site.register(Group, GroupAdmin)
