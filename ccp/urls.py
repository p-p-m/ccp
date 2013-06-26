from django.conf.urls.defaults import patterns, include, url
from django.contrib import admin
from django.contrib.auth import views as auth_views
# from django.contrib.auth.forms import EmailAuthenticationForm
from django.conf.urls.static import static

import settings

admin.autodiscover()

urlpatterns = patterns(
    '',
    # pages:
    url(r'^login/$',
        auth_views.login,
        name='login',),
    url(r'', include('bio.urls')),
) + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
