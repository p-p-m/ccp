from django.conf.urls.defaults import patterns, url

import views

urlpatterns = patterns(
    '',
    url(r'$',
        views.personal_data,
        name='index'),
)
