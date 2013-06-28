from django.core.urlresolvers import reverse


def edit_link(obj):
    '''
    Returns link ti admin edit page
    >>> from django.contrib.auth.models import User
    >>> adm = User.objects.get(id=1)
    >>> edit_link(adm)
    '/admin/auth/user/1/'
    '''

