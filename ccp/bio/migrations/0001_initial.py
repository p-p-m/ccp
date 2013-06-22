# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'PersonalData'
        db.create_table('bio_personaldata', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=50)),
            ('birthdate', self.gf('django.db.models.fields.DateField')()),
            ('surname', self.gf('django.db.models.fields.CharField')(max_length=500)),
            ('email', self.gf('django.db.models.fields.EmailField')(max_length=75)),
            ('skype', self.gf('django.db.models.fields.CharField')(max_length=50)),
            ('other_contacts', self.gf('django.db.models.fields.CharField')(max_length=200)),
            ('jabber', self.gf('django.db.models.fields.CharField')(max_length=50)),
        ))
        db.send_create_signal('bio', ['PersonalData'])


    def backwards(self, orm):
        # Deleting model 'PersonalData'
        db.delete_table('bio_personaldata')


    models = {
        'bio.personaldata': {
            'Meta': {'object_name': 'PersonalData'},
            'birthdate': ('django.db.models.fields.DateField', [], {}),
            'email': ('django.db.models.fields.EmailField', [], {'max_length': '75'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'jabber': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            'other_contacts': ('django.db.models.fields.CharField', [], {'max_length': '200'}),
            'skype': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            'surname': ('django.db.models.fields.CharField', [], {'max_length': '500'})
        }
    }

    complete_apps = ['bio']