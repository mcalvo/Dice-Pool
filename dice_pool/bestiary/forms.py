from django.core.exceptions import ValidationError
from django.db import models
from django import forms
from bestiary import choices
from bestiary import models as mcm
from bestiary import helpers as bhelpers
import math, random

class MonsterForm(forms.ModelForm):
   def save(self, *args, **kwargs):
      record = super(MonsterForm, self).save(commit=False, *args, **kwargs)
      if not self.instance.id:   
         random.seed()
         record.initiative = record.level*.60
         record.hp = bhelpers.hpCalc(record.level, record.role, record.minion, record.elite, record.solo)
         record.gibHP = bhelpers.gibCalc(record.hp, record.role.gibRatio, record.minion, record.elite, record.solo)
         
         #Calculate our defenses
         record.ac = bhelpers.defenseCalc(14, record.role.acModMin, record.role.acModMax, record.level, record.elite, record.solo)
         record.fortitude = bhelpers.defenseCalc(12, record.role.fortModMin, record.role.fortModMax, record.level, record.elite, record.solo)
         record.reflex = bhelpers.defenseCalc(12,record.role.refModMin, record.role.refModMax, record.level, record.elite, record.solo) 
         record.will = bhelpers.defenseCalc(12,record.role.willModMin, record.role.willModMax, record.level, record.elite, record.solo)
         
         #Attack bonuses
         record.acAtkBase = random.randint(-1, 1) + record.level + 5
         record.nacAtkBase = random.randint(-1, 1) + record.level + 3
         
         #Skill DC for opposed checks (Save on rolls)
         record.eDC = 7 + round(record.level * .53)
         record.mDC = 12 + round(record.level * .53) + round(record.level/10)
         record.hDC = 17 + round(record.level *.64) + round(record.level/5)
      record.save()
   
   class Meta:
      model = mcm.Monster
      fields = ('name', 'level', 'role', 'minion', 'elite', 'solo', 'speed')

class AbilityForm(forms.ModelForm):
   
   def __init__(self, monster, *args, **kwargs):
      self.monster = monster
      super(AbilityForm, self).__init__(*args, **kwargs)    

   def clean(self):
      range = self.cleaned_data.get('range')
      area = self.cleaned_data.get('area')
      
      if range < 0:
         raise forms.ValidationError("Range minimum is 0.")
      
      if area < 0:
         raise forms.ValidationError("Area minimum is 0.")
      
      return self.cleaned_data 
        
   def save(self, *args, **kwargs):
      record = super(AbilityForm, self).save(commit=False,*args,**kwargs)
      #Brand new, needs to be processed.
      if not self.instance.id:   
         record.monster = self.monster
      record.save()

   class Meta:
      model = mcm.Ability
      exclude = ['monster']

class AttackForm(forms.ModelForm):
   
   def __init__(self, monster, *args, **kwargs):
      self.monster = monster
      super(AttackForm, self).__init__(*args, **kwargs)    

   def clean(self):
      range = self.cleaned_data.get('range')
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
         record.attackBonus = bhelpers.toHit(record.monster,record.range, record.area, record.isRanged, record.targetDefense)
         hasEffect = True if record.effect or record.aftereffect or record.onHit else False  
         #For calculations and short hand if combat drags on.
         record.averageDamage = bhelpers.averageDamage(record.monster, record.monster.role.heavyHitter, record.range,record.area,record.usage.limitedUsage, record.bloodiedLimit, record.multiStrike,hasEffect)
         record.damageLine = bhelpers.damageToDice(record.averageDamage,record.monster.minion,record.onHit)
      record.save()

   class Meta:
      model = mcm.Attack
      exclude = ['monster', 'attackBonus', 'damageLine', 'averageDamage']
