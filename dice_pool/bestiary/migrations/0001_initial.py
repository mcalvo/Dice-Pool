# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'MonsterRole'
        db.create_table('bestiary_monsterrole', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=50)),
            ('active', self.gf('django.db.models.fields.BooleanField')(default=True)),
            ('hpBase', self.gf('django.db.models.fields.IntegerField')()),
            ('hpRatio', self.gf('django.db.models.fields.DecimalField')(max_digits=3, decimal_places=2)),
            ('gibRatio', self.gf('django.db.models.fields.DecimalField')(max_digits=3, decimal_places=2)),
            ('acModMin', self.gf('django.db.models.fields.IntegerField')()),
            ('acModMax', self.gf('django.db.models.fields.IntegerField')()),
            ('fortModMin', self.gf('django.db.models.fields.IntegerField')()),
            ('fortModMax', self.gf('django.db.models.fields.IntegerField')()),
            ('refModMin', self.gf('django.db.models.fields.IntegerField')()),
            ('refModMax', self.gf('django.db.models.fields.IntegerField')()),
            ('willModMin', self.gf('django.db.models.fields.IntegerField')()),
            ('willModMax', self.gf('django.db.models.fields.IntegerField')()),
            ('heavyHitter', self.gf('django.db.models.fields.BooleanField')(default=False)),
        ))
        db.send_create_signal('bestiary', ['MonsterRole'])

        # Adding model 'Faction'
        db.create_table('bestiary_faction', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=50)),
            ('active', self.gf('django.db.models.fields.BooleanField')(default=True)),
        ))
        db.send_create_signal('bestiary', ['Faction'])

        # Adding model 'Monster'
        db.create_table('bestiary_monster', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=50)),
            ('level', self.gf('django.db.models.fields.IntegerField')()),
            ('role', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['bestiary.MonsterRole'])),
            ('faction', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['bestiary.Faction'])),
            ('minion', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('elite', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('solo', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('initiative', self.gf('django.db.models.fields.IntegerField')()),
            ('speed', self.gf('django.db.models.fields.IntegerField')()),
            ('hp', self.gf('django.db.models.fields.IntegerField')()),
            ('gibHP', self.gf('django.db.models.fields.IntegerField')()),
            ('ac', self.gf('django.db.models.fields.IntegerField')()),
            ('fortitude', self.gf('django.db.models.fields.IntegerField')()),
            ('reflex', self.gf('django.db.models.fields.IntegerField')()),
            ('will', self.gf('django.db.models.fields.IntegerField')()),
            ('acAtkBase', self.gf('django.db.models.fields.IntegerField')()),
            ('nacAtkBase', self.gf('django.db.models.fields.IntegerField')()),
            ('eDC', self.gf('django.db.models.fields.IntegerField')()),
            ('mDC', self.gf('django.db.models.fields.IntegerField')()),
            ('hDC', self.gf('django.db.models.fields.IntegerField')()),
        ))
        db.send_create_signal('bestiary', ['Monster'])


    def backwards(self, orm):
        # Deleting model 'MonsterRole'
        db.delete_table('bestiary_monsterrole')

        # Deleting model 'Faction'
        db.delete_table('bestiary_faction')

        # Deleting model 'Monster'
        db.delete_table('bestiary_monster')


    models = {
        'bestiary.faction': {
            'Meta': {'ordering': "['-active', 'name']", 'object_name': 'Faction'},
            'active': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '50'})
        },
        'bestiary.monster': {
            'Meta': {'object_name': 'Monster'},
            'ac': ('django.db.models.fields.IntegerField', [], {}),
            'acAtkBase': ('django.db.models.fields.IntegerField', [], {}),
            'eDC': ('django.db.models.fields.IntegerField', [], {}),
            'elite': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'faction': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['bestiary.Faction']"}),
            'fortitude': ('django.db.models.fields.IntegerField', [], {}),
            'gibHP': ('django.db.models.fields.IntegerField', [], {}),
            'hDC': ('django.db.models.fields.IntegerField', [], {}),
            'hp': ('django.db.models.fields.IntegerField', [], {}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'initiative': ('django.db.models.fields.IntegerField', [], {}),
            'level': ('django.db.models.fields.IntegerField', [], {}),
            'mDC': ('django.db.models.fields.IntegerField', [], {}),
            'minion': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'nacAtkBase': ('django.db.models.fields.IntegerField', [], {}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            'reflex': ('django.db.models.fields.IntegerField', [], {}),
            'role': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['bestiary.MonsterRole']"}),
            'solo': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'speed': ('django.db.models.fields.IntegerField', [], {}),
            'will': ('django.db.models.fields.IntegerField', [], {})
        },
        'bestiary.monsterrole': {
            'Meta': {'ordering': "['-active', 'name']", 'object_name': 'MonsterRole'},
            'acModMax': ('django.db.models.fields.IntegerField', [], {}),
            'acModMin': ('django.db.models.fields.IntegerField', [], {}),
            'active': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'fortModMax': ('django.db.models.fields.IntegerField', [], {}),
            'fortModMin': ('django.db.models.fields.IntegerField', [], {}),
            'gibRatio': ('django.db.models.fields.DecimalField', [], {'max_digits': '3', 'decimal_places': '2'}),
            'heavyHitter': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'hpBase': ('django.db.models.fields.IntegerField', [], {}),
            'hpRatio': ('django.db.models.fields.DecimalField', [], {'max_digits': '3', 'decimal_places': '2'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            'refModMax': ('django.db.models.fields.IntegerField', [], {}),
            'refModMin': ('django.db.models.fields.IntegerField', [], {}),
            'willModMax': ('django.db.models.fields.IntegerField', [], {}),
            'willModMin': ('django.db.models.fields.IntegerField', [], {})
        }
    }

    complete_apps = ['bestiary']