# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Request'
        db.create_table('bio_request', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('meta', self.gf('django.db.models.fields.CharField')(max_length=2000)),
            ('body', self.gf('django.db.models.fields.CharField')(max_length=2000)),
            ('path', self.gf('django.db.models.fields.CharField')(max_length=500)),
            ('date_added', self.gf('django.db.models.fields.DateField')(auto_now_add=True, blank=True)),
        ))
        db.send_create_signal('bio', ['Request'])


    def backwards(self, orm):
        # Deleting model 'Request'
        db.delete_table('bio_request')


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
            'body': ('django.db.models.fields.CharField', [], {'max_length': '2000'}),
            'date_added': ('django.db.models.fields.DateField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'meta': ('django.db.models.fields.CharField', [], {'max_length': '2000'}),
            'path': ('django.db.models.fields.CharField', [], {'max_length': '500'})
        }
    }

    complete_apps = ['bio']