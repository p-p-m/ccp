# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding field 'PersonalData.bio'
        db.add_column('bio_personaldata', 'bio',
                      self.gf('django.db.models.fields.CharField')(max_length=500, null=True),
                      keep_default=False)


        # Changing field 'PersonalData.surname'
        db.alter_column('bio_personaldata', 'surname', self.gf('django.db.models.fields.CharField')(max_length=50))

    def backwards(self, orm):
        # Deleting field 'PersonalData.bio'
        db.delete_column('bio_personaldata', 'bio')


        # Changing field 'PersonalData.surname'
        db.alter_column('bio_personaldata', 'surname', self.gf('django.db.models.fields.CharField')(max_length=500))

    models = {
        'bio.personaldata': {
            'Meta': {'object_name': 'PersonalData'},
            'bio': ('django.db.models.fields.CharField', [], {'max_length': '500', 'null': 'True'}),
            'birthdate': ('django.db.models.fields.DateField', [], {}),
            'email': ('django.db.models.fields.EmailField', [], {'max_length': '75'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'jabber': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            'other_contacts': ('django.db.models.fields.CharField', [], {'max_length': '200'}),
            'skype': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            'surname': ('django.db.models.fields.CharField', [], {'max_length': '50'})
        }
    }

    complete_apps = ['bio']