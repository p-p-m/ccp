import sys

from django.core.management.base import BaseCommand
from django.db import models


def _print(s):
    sys.stdout.write(s+'\n')
    sys.stderr.write('error:'+s+'\n')


class Command(BaseCommand):
    args = 'no args for this command'
    help = 'Shows list of django models and objects count in them'

    def handle(self, *args, **options):
        for m in models.get_models():
            _print(":".join([m.__name__, str(m.objects.count())]))
