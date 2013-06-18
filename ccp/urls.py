from django.conf.urls.defaults import patterns, include, url
from django.contrib import admin

from django.conf.urls.static import static
from django.views.generic.base import TemplateView

import settings

admin.autodiscover()

urlpatterns = patterns(
    '',
    # static pages:
    url(r'^$', TemplateView.as_view(template_name="index.html"), name='index'),
) + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
