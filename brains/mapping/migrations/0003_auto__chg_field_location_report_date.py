# encoding: utf-8
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models

class Migration(SchemaMigration):

    def forwards(self, orm):
        
        # Changing field 'Location.report_date'
        db.alter_column('mapping_location', 'report_date', self.gf('django.db.models.fields.DateTimeField')(auto_now=True, null=True))


    def backwards(self, orm):
        
        # Changing field 'Location.report_date'
        db.alter_column('mapping_location', 'report_date', self.gf('django.db.models.fields.DateTimeField')(default=None, auto_now=True))


    models = {
        'mapping.location': {
            'Meta': {'unique_together': "(('x', 'y'),)", 'object_name': 'Location'},
            'barricade_level': ('django.db.models.fields.PositiveSmallIntegerField', [], {'default': '0'}),
            'building_type': ('django.db.models.fields.CharField', [], {'max_length': '4'}),
            'has_tree': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'is_illuminated': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'is_ruined': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '300'}),
            'report_date': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'null': 'True', 'blank': 'True'}),
            'x': ('django.db.models.fields.PositiveSmallIntegerField', [], {}),
            'y': ('django.db.models.fields.PositiveSmallIntegerField', [], {}),
            'zombies_present': ('django.db.models.fields.PositiveIntegerField', [], {'default': '0'})
        }
    }

    complete_apps = ['mapping']
