# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding field 'PersonalData.photo'
        db.add_column('bio_personaldata', 'photo',
                      self.gf('django.db.models.fields.files.FileField')(max_length=100, null=True),
                      keep_default=False)


    def backwards(self, orm):
        # Deleting field 'PersonalData.photo'
        db.delete_column('bio_personaldata', 'photo')


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
            'photo': ('django.db.models.fields.files.FileField', [], {'max_length': '100', 'null': 'True'}),
            'skype': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            'surname': ('django.db.models.fields.CharField', [], {'max_length': '50'})
        },
        'bio.request': {
            'Meta': {'object_name': 'Request'},
            'date_added': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'meta': ('django.db.models.fields.CharField', [], {'max_length': '2000'}),
            'path': ('django.db.models.fields.CharField', [], {'max_length': '500'})
        }
    }

    complete_apps = ['bio']