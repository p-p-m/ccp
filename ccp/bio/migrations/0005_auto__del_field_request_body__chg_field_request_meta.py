# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Deleting field 'Request.body'
        db.delete_column('bio_request', 'body')


        # Changing field 'Request.meta'
        db.alter_column('bio_request', 'meta', self.gf('django.db.models.fields.TextField')())

    def backwards(self, orm):

        # User chose to not deal with backwards NULL issues for 'Request.body'
        raise RuntimeError("Cannot reverse this migration. 'Request.body' and its values cannot be restored.")

        # Changing field 'Request.meta'
        db.alter_column('bio_request', 'meta', self.gf('django.db.models.fields.CharField')(max_length=2000))

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
        },
        'bio.request': {
            'Meta': {'object_name': 'Request'},
            'date_added': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'meta': ('django.db.models.fields.TextField', [], {}),
            'path': ('django.db.models.fields.CharField', [], {'max_length': '500'})
        }
    }

    complete_apps = ['bio']