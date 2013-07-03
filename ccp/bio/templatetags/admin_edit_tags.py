from django.core.urlresolvers import reverse
from django import template

register = template.Library()


@register.simple_tag
def edit_link(obj):
    '''
    Returns link to admin edit page
    '''
    app = obj._meta.app_label
    module = obj._meta.module_name
    return reverse(
        'admin:{0}_{1}_change'.format(app, module), args=[obj.id])
