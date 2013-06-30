from django.db import models
from django.db.models.signals import post_save, post_delete
from django.db.utils import DatabaseError
from django.dispatch.dispatcher import receiver


class PersonalData(models.Model):
    name = models.CharField(max_length=50)
    surname = models.CharField(max_length=50)
    birthdate = models.DateField()
    bio = models.CharField(max_length=500, null=True, blank=True)
    email = models.EmailField()
    skype = models.CharField(max_length=50)
    other_contacts = models.CharField(max_length=200)
    jabber = models.CharField(max_length=50)
    photo = models.FileField(upload_to='myphoto', null=True, blank=True)


class Request(models.Model):
    meta = models.TextField()
    path = models.CharField(max_length=500)
    date_added = models.DateTimeField(auto_now_add=True)

    class Meta:
        get_latest_by = "date_added"


class DBSignal(models.Model):
    table_name = models.CharField(max_length=100)
    status = models.CharField(
        max_length=20,
        choices=(('created',)*2, ('modified',)*2, ('deleted',)*2))
    date_added = models.DateTimeField(auto_now_add=True)

    class Meta:
        get_latest_by = "date_added"


def _db_signal(status, kwargs):
    if DBSignal in models.get_models():
        table_name = kwargs['instance'].__class__.__name__
        if table_name != 'DBSignal':
            # this try alows to awoid errors, when dbsignal table
            # isn`t created from migrations, but other app tries to add
            # some data from fixtures
            try:
                sign = DBSignal(table_name=table_name, status=status)
                sign.save()
            except DatabaseError as er:
                if str(er) == 'no such table: bio_dbsignal':
                    pass
                else:
                    raise er


@receiver(post_save)
def create_update_signal(sender, **kwargs):
    status = 'created' if kwargs['created'] else 'modified'
    _db_signal(status, kwargs)


@receiver(post_delete)
def delete_signal(sender, **kwargs):
    _db_signal('deleted', kwargs)
