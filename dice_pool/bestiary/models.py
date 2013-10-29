from django.core.exceptions import ValidationError
from django.db import models
from django import forms
from django.forms import ModelForm
from bestiary import choices
from bestiary import helpers as bhelpers
import math, random

class ActiveDefinitionManager(models.Manager):
   def get_query_set(self):
      return super(ActiveDefinitionManager, self).get_query_set().filter(active=True)

class InactiveDefinitionManager(models.Manager):
   def get_query_set(self):
      return super(ActiveDefinitionManager, self).get_query_set().filter(active=False)

class Definition(models.Model):
   name = models.CharField(max_length=50)
   active = models.BooleanField(default=True)
   objects = ActiveDefinitionManager()
   all_objects = models.Manager()

   def __unicode__(self):
      if not self.active:
         return '%s (Inactive)' % self.name
      return '%s' % self.name
   
   class Meta:
      ordering = ['-active', 'name']
      abstract = True

class MonsterRole(Definition):
   hpBase = models.IntegerField()
   hpRatio = models.DecimalField("HP per level", max_digits=3, decimal_places=2)
   gibRatio = models.DecimalField("Chunky Salsa Number",max_digits=3, decimal_places=2, help_text="Percentage of health needed to be done in a single attack to kill the target outright")
   acModMin = models.IntegerField("AC Adjustment Minimum")
   acModMax = models.IntegerField("AC Adjustment Maximum")
   fortModMin = models.IntegerField("Fortitude Adjustment Minimum")
   fortModMax = models.IntegerField("Fortitude Adjustment Minimum")
   refModMin = models.IntegerField("Reflex Adjustment Minimum")
   refModMax = models.IntegerField("Reflex Adjustment Minimum")
   willModMin = models.IntegerField("Will Adjustment Minimum")
   willModMax = models.IntegerField("Will Adjustment Minimum")
   heavyHitter = models.BooleanField("Sacrifice accuracy for damage?") #For brutes, mostly.
   
   def __unicode__(self):
      if heavyHitter:
         return "Brute %s" % self.name
      return "%s" % self.name
      
   def save(self, *args, **kwargs):
      if self.acModMin >= self.acModMax:
         self.acModMin = self.acModMax - 3
      
      if self.fortModMin >= self.fortModMax:
         self.fortModMin = self.fortModMax - 3
      
      if self.refModMin >= self.refModMax:
         self.refModMin = self.refModMax - 3
      
      if self.willModMin >= self.willModMax:
         self.willModMin = self.willModMax - 3

class Faction(Definition):
   pass

class Monster(models.Model):
   name = models.CharField(max_length = 50)
   level = models.IntegerField()
   role = models.ForeignKey(MonsterRole)
   faction = models.ForeignKey(Faction)
   minion = models.BooleanField(verbose_name = 'Minion?')
   elite = models.BooleanField(verbose_name = 'Elite?')
   solo = models.BooleanField(verbose_name = 'Solo?')
   initiative = models.IntegerField(verbose_name = 'Initiative')
   speed = models.IntegerField(verbose_name = 'Speed')
   hp = models.IntegerField(verbose_name = 'Health')
   gibHP = models.IntegerField(verbose_name = 'Insta-gib HP')
   ac = models.IntegerField(verbose_name = 'Armor Class')
   fortitude = models.IntegerField(verbose_name = 'Fortitude')
   reflex = models.IntegerField(verbose_name = 'Reflex')
   will = models.IntegerField(verbose_name = 'Will')
   acAtkBase = models.IntegerField(verbose_name = 'Base Attack Bonus vs. AC')
   nacAtkBase = models.IntegerField(verbose_name = 'Base Attack Bonus vs. NAD')
   eDC = models.IntegerField(verbose_name = 'Easy DC')
   mDC = models.IntegerField(verbose_name = 'Medium DC')
   hDC = models.IntegerField(verbose_name = 'Hard DC')
    
   def __unicode__(self):
      return "Lvl. %s %s" % (self.level, self.name)
   
   def __rebalance(self, level, role, minion, elite, solo):
      self.level = level
      self.role = role
      self.minion = minion
      self.elite = elite
      self.solo = solo
      self.initiative = level * .60
      self.hp = bhelpers.hpCalc(level, role, minion, elite, solo)
      self.gibHP = bhelpers.gibCalc(self.hp, self.role.gibRatio, minion, elite, solo)
      self.ac = bhelpers.defenseCalc(14, self.role.acModMin, acModMax, self.level)
      self.fortitude = bhelpers.defenseCalc(12, self.role.fortModMin, self.role.fortModMax, self.level)
      self.reflex = bhelpers.defenseCalc(12,self.role.refModMin, self.role.refModMax, self.level) 
      self.will = bhelpers.defenseCalc(12,self.role.willModMin, self.role.willModMax, self.level)     
      self.acAtkBase = random.randint(-1, 1) + level + 5
      self.nacAtkBase = random.randint(-1, 1) + level + 3
      self.eDC = 7 + round(level * .53)
      self.mDC = 12 + round(level * 53) + round(level/10)
      self.hDC = 17 + round(level *.64) + round(level/5)
      self.save()

"""
class Attack(models.Model):
    monster = models.ForeignKey(Monster)
    name = models.CharField(max_length = 20)
    attackType = models.CharField(max_length = 3, choices = choices.ATTACK_TYPES)
    attackRange = models.CharField(max_length=10)
    #Which defense the target attacks
    tardef = models.CharField(verbose_name = 'target defense', max_length = 1, choices = choices.DEFENSES) 
    use = models.CharField(max_length = 2, choices = choices.USABILITY)
    action = models.CharField(max_length = 2, choices = choices.ACTION)
    multi_attack = models.BooleanField()
    atkBonus = models.IntegerField()
    damage = models.CharField(max_length = 30)
    avg_dmg = models.IntegerField()
    effects = models.CharField(verbose_name = 'Additional Effects', blank=True, null=True, max_length = 70)

    def __unicode__(self):
        return self.name

"""
