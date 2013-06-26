from django.db import models


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
    meta = models.CharField(max_length=2000)
    body = models.CharField(max_length=2000)
    path = models.CharField(max_length=500)
    date_added = models.DateTimeField(auto_now_add=True)

    class Meta:
        get_latest_by = "date_added"
