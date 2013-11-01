from django.core.exceptions import ValidationError
from django.db import models
from django import forms
from bestiary import choices
from bestiary import models as mcm
from bestiary import helpers as bhelpers
import math, random

class MonsterForm(forms.ModelForm):
   level = forms.IntegerField(label='Level', min_value=1, max_value=50)

   def save(self, *args, **kwargs):
      record = super(MonsterForm, self).save(commit=False, *args, **kwargs)
      if record:
         random.seed()
         record.initiative = record.level*.60
         record.hp = bhelpers.hpCalc(record.level, record.role, record.minion, record.elite, record.solo)
         record.gibHP = bhelpers.gibCalc(record.hp, record.role, record.minion, record.elite, record.solo)
         record.ac = bhelpers.defenseCalc(14, record.role.acModMin, acModMax, record.level)
         record.fortitude = bhelpers.defenseCalc(12, record.role.fortModMin, record.role.fortModMax, record.level)
         record.reflex = bhelpers.defenseCalc(12,record.role.refModMin, record.role.refModMax, record.level) 
         record.will = bhelpers.defenseCalc(12,record.role.willModMin, record.role.willModMax, record.level)
         record.acAtkBase = random.randint(-1, 1) + record.level + 5
         record.nacAtkBase = random.randint(-1, 1) + record.level + 3
         record.eDC = 7 + round(record.level * .53)
         record.mDC = 12 + round(record.level * 53) + round(record.level/10)
         record.hDC = 17 + round(record.level *.64) + round(record.level/5)
      record.save(*args, **kwargs)

    class Meta:
        model = mcm.Monster
        fields = ('name', 'level', 'role', 'minion', 'elite', 'solo', 'speed')
        #exclude = ('ac', 'fortitude', 'reflex', 'will', 'initiative', 'hp', 'suddenDmg', 'acAtkBase', 'nacAtkBase', 'eDC', 'mDC', 'hDC',)

class AttackForm(forms.ModelForm):
   def __init__(self, monster, *args, **kwargs):
      super(AttackForm, self).__init__(*args, **kwargs)
      self.monster = monster
   
   def clean(self):
      range = self.cleaned_date.get('range')
      area = self.cleaned_data.get('area')
      
      if range < 0:
         raise forms.ValidationError("Range minimum is 0.")
      
      if area < 0:
         raise forms.ValidationError("Area minimum is 0.")
      
      return self.cleaned_data 
        
    def save(self, *args, **kwargs):
      record = super(AttackForm, self).save(commit=False,*args,**kwargs)
      #Brand new, needs to be processed.
      if not self.instance.id:   
         record.monster = self.monster
         record.attackBonus = bhelpers.toHit(record.monster,record.range,record.targetDef)
         hasEffect = True if record.effect or record.aftereffect or record.onHit else False  
         record.averageDamage = bhelpers.averageDamage(record.monster.level,record.monster.minion,record.monster.role.heavyHitter,record.range,record.area,self.limited,record.multiStrike,hasEffect)
         record.damageLine = bhelpers.damageToDice(record.averageDamage,record.monster.minion,record.onHit)
      record.save()

   class Meta:
      model = mcm.Attack
      exclude = ['monster', 'attackBonus', 'damageLine']
