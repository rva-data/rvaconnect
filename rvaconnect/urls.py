from django.conf.urls import patterns, include, url
from django.conf import settings
from django.contrib import admin
from django.views.generic.base import TemplateView

admin.autodiscover()

urlpatterns = patterns('',
    url(r'{0}'.format(settings.ADMIN_URL_PATH), include(admin.site.urls)),
    url(r'^$', view=TemplateView.as_view(template_name="holder.html"), name='holder'),
)
