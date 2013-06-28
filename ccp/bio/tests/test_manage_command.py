import sys
from cStringIO import StringIO

from django.core.management import call_command
from django.db import models


def test_modelscount_command():

    # saving stdout for as redirext output
    old_stdout = sys.stdout
    redirected_output = sys.stdout = StringIO()
    call_command('modelscount')
    sys.stdout = old_stdout

    l = lambda m: ':'.join([m.__name__, str(m.objects.count())])
    expected = '\n'.join(map(l, models.get_models()))
    assert expected.strip() == redirected_output.getvalue().strip()
