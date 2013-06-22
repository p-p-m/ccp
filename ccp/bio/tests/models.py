from django.db import models


class PersonalData(models.Model):
    name = models.CharField(max_length=50)
    surname = models.CharField(max_length=50)
    birthdate = models.DateField()
    surname = models.CharField(max_length=500)
    email = models.EmailField()
    skype = models.CharField(max_length=50)
    other_contacts = models.CharField(max_length=200)
    jabber = models.CharField(max_length=50)
