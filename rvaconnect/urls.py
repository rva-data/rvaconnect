from django.conf.urls import patterns, include, url
from django.contrib import admin
from django.views.generic.base import TemplateView

admin.autodiscover()

urlpatterns = patterns('',
    url(r'^admin/', include(admin.site.urls)),
    url(r'', view=TemplateView.as_view(template_name="holder.html"), name='holder'),
)
