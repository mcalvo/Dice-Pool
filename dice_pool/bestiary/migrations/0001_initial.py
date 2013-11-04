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

        # Adding model 'Monster'
        db.create_table('bestiary_monster', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=100)),
            ('level', self.gf('django.db.models.fields.IntegerField')()),
            ('role', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['bestiary.MonsterRole'])),
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

        # Adding model 'Usage'
        db.create_table('bestiary_usage', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=50)),
            ('active', self.gf('django.db.models.fields.BooleanField')(default=True)),
            ('limitedUsage', self.gf('django.db.models.fields.BooleanField')(default=False)),
        ))
        db.send_create_signal('bestiary', ['Usage'])

        # Adding model 'Ability'
        db.create_table('bestiary_ability', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=70, null=True, blank=True)),
            ('monster', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['bestiary.Monster'])),
            ('usage', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['bestiary.Usage'])),
            ('action', self.gf('django.db.models.fields.CharField')(max_length=2)),
            ('range', self.gf('django.db.models.fields.IntegerField')()),
            ('area', self.gf('django.db.models.fields.IntegerField')()),
            ('bloodiedLimit', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('isRanged', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('oaFlag', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('aura', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('effect', self.gf('django.db.models.fields.CharField')(max_length=150, null=True, blank=True)),
            ('aftereffect', self.gf('django.db.models.fields.CharField')(max_length=150, null=True, blank=True)),
        ))
        db.send_create_signal('bestiary', ['Ability'])

        # Adding model 'Attack'
        db.create_table('bestiary_attack', (
            ('ability_ptr', self.gf('django.db.models.fields.related.OneToOneField')(to=orm['bestiary.Ability'], unique=True, primary_key=True)),
            ('attackBonus', self.gf('django.db.models.fields.IntegerField')()),
            ('targetDefense', self.gf('django.db.models.fields.CharField')(max_length=1)),
            ('averageDamage', self.gf('django.db.models.fields.IntegerField')()),
            ('damageLine', self.gf('django.db.models.fields.CharField')(max_length=150)),
            ('multiStrike', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('onHit', self.gf('django.db.models.fields.CharField')(max_length=150, null=True, blank=True)),
        ))
        db.send_create_signal('bestiary', ['Attack'])


    def backwards(self, orm):
        # Deleting model 'MonsterRole'
        db.delete_table('bestiary_monsterrole')

        # Deleting model 'Monster'
        db.delete_table('bestiary_monster')

        # Deleting model 'Usage'
        db.delete_table('bestiary_usage')

        # Deleting model 'Ability'
        db.delete_table('bestiary_ability')

        # Deleting model 'Attack'
        db.delete_table('bestiary_attack')


    models = {
        'bestiary.ability': {
            'Meta': {'object_name': 'Ability'},
            'action': ('django.db.models.fields.CharField', [], {'max_length': '2'}),
            'aftereffect': ('django.db.models.fields.CharField', [], {'max_length': '150', 'null': 'True', 'blank': 'True'}),
            'area': ('django.db.models.fields.IntegerField', [], {}),
            'aura': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'bloodiedLimit': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'effect': ('django.db.models.fields.CharField', [], {'max_length': '150', 'null': 'True', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'isRanged': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'monster': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['bestiary.Monster']"}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '70', 'null': 'True', 'blank': 'True'}),
            'oaFlag': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'range': ('django.db.models.fields.IntegerField', [], {}),
            'usage': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['bestiary.Usage']"})
        },
        'bestiary.attack': {
            'Meta': {'object_name': 'Attack', '_ormbases': ['bestiary.Ability']},
            'ability_ptr': ('django.db.models.fields.related.OneToOneField', [], {'to': "orm['bestiary.Ability']", 'unique': 'True', 'primary_key': 'True'}),
            'attackBonus': ('django.db.models.fields.IntegerField', [], {}),
            'averageDamage': ('django.db.models.fields.IntegerField', [], {}),
            'damageLine': ('django.db.models.fields.CharField', [], {'max_length': '150'}),
            'multiStrike': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'onHit': ('django.db.models.fields.CharField', [], {'max_length': '150', 'null': 'True', 'blank': 'True'}),
            'targetDefense': ('django.db.models.fields.CharField', [], {'max_length': '1'})
        },
        'bestiary.monster': {
            'Meta': {'object_name': 'Monster'},
            'ac': ('django.db.models.fields.IntegerField', [], {}),
            'acAtkBase': ('django.db.models.fields.IntegerField', [], {}),
            'eDC': ('django.db.models.fields.IntegerField', [], {}),
            'elite': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
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
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
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
        },
        'bestiary.usage': {
            'Meta': {'ordering': "['-active', 'name']", 'object_name': 'Usage'},
            'active': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'limitedUsage': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '50'})
        }
    }

    complete_apps = ['bestiary']