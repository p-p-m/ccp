from django.core.urlresolvers import reverse
from django import template

register = template.Library()


@register.simple_tag
def edit_link(obj):
    '''
    Returns link ti admin edit page
    >>> from django.contrib.auth.models import User
    >>> adm = User.objects.get(id=1)
    >>> edit_link(adm)
    '/admin/auth/user/1/'
    '''
    app = obj._meta.app_label
    module = obj._meta.module_name
    return reverse(
        'admin:{0}_{1}_change'.format(app, module), args=[obj.id])
