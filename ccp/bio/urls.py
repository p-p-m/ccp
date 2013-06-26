from django.conf.urls.defaults import patterns, url

import views

urlpatterns = patterns(
    '',
    url(r'^$',
        views.personal_data,
        name='index'),
    url(r'requests/$',
        views.stored_requests,
        name='stored_requests'),
    url(r'personal-data/update/$',
        views.personal_data_update,
        name='personal_data_update'),
)
