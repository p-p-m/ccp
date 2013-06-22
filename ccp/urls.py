from django.conf.urls.defaults import patterns, include, url
from django.contrib import admin

from django.conf.urls.static import static

import settings

admin.autodiscover()

urlpatterns = patterns(
    '',
    # pages:
    url(r'^', include('bio.urls')),
) + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
