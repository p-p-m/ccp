import sys
import subprocess
import os
from datetime import date
from cStringIO import StringIO

from django.core.management import call_command
from django.db import models
from django.conf import settings


def _output(attr):
    ''' saving sys attr for as redirected and returns it '''
    old_std = getattr(sys, attr)
    redirected = StringIO()
    setattr(sys, attr, redirected)
    call_command('modelscount')
    setattr(sys, attr, old_std)
    return redirected


def _modelscount():
    l = lambda m: ':'.join([m.__name__, str(m.objects.count())])
    return map(l, models.get_models())


def test_modelscount_command():
    # saving stdout for as redirext output
    for attr in ('stdout', 'stderr'):
        redirected = _output(attr)
        l = lambda m: ':'.join([m.__name__, str(m.objects.count())])
        prefix = 'error:' if attr == 'stderr' else ''
        expected = prefix + ('\n' + prefix).join(_modelscount())
        assert expected.strip() == redirected.getvalue().strip()


def test_bash_script():
    subprocess.call(
        ['sh', os.path.join(settings.PROJECT_PATH, 'modelscount.sh')])
    fname = date.today().strftime('%m.%d.%Y') + '.dat'
    f = open(os.path.join(settings.PROJECT_PATH, fname), 'rb')
    names = [m.__name__ for m in models.get_models()]
    for l in f:
        print 'l', l
    for l, n in zip(f, names):
        assert n in l, 'n = ' + str(n) + '\n l = ' + str(l)
    f.close()
    os.remove(f.name)
