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
      super(MonsterRole, self).save(*args, **kwargs)

class Monster(models.Model):
   name = models.CharField(max_length = 100)
   level = models.IntegerField()
   role = models.ForeignKey(MonsterRole)
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
   
   def __rebalance__(self):
      self.initiative = self.level * .60
      self.hp = bhelpers.hpCalc(self.level, self.role, self.minion, self.elite, self.solo)
      self.gibHP = bhelpers.gibCalc(self.hp, self.role.gibRatio, self.minion, self.elite, self.solo)
      self.ac = bhelpers.defenseCalc(14, self.role.acModMin, self.role.acModMax, self.level, self.elite, self.solo)
      self.fortitude = bhelpers.defenseCalc(12, self.role.fortModMin, self.role.fortModMax, self.level, self.elite, self.solo)
      self.reflex = bhelpers.defenseCalc(12,self.role.refModMin, self.role.refModMax, self.level, self.elite, self.solo) 
      self.will = bhelpers.defenseCalc(12,self.role.willModMin, self.role.willModMax, self.level, self.elite, self.solo)     
      self.acAtkBase = random.randint(-1, 1) + self.level + 5
      self.nacAtkBase = random.randint(-1, 1) + self.level + 3
      self.eDC = 7 + round(self.level * .53)
      self.mDC = 12 + round(self.level * .53) + round(self.level/10)
      self.hDC = 17 + round(self.level *.64) + round(self.level/5)
      self.save()
      
      for attack in self.attack_set.all():
         attack.__rebalance__()

class Usage(Definition):
   limitedUsage = models.BooleanField("Limited")
   triggeredAction = models.BooleanField("Triggered?")
 
class PowerBase(models.Model):
   name = models.CharField(max_length=70, blank=True, null=True)
   monster = models.ForeignKey(Monster)
   usage = models.ForeignKey(Usage)
   action = models.CharField(max_length=2,choices=choices.ACTION)
   range = models.IntegerField()#0 for Personal, 1 for Melee
   area = models.IntegerField()#0 for Single Target, 1 for Burst/Blast 1, etc. 
   bloodiedLimit = models.BooleanField("Only usable when bloodied?")
   isRanged = models.BooleanField("Considered a Ranged Attack?")
   isPassive = models.BooleanField("A passive ability?")
   oaFlag = models.BooleanField("Provokes Opportunity Attack?")
   aura = models.BooleanField("Is an Aura?")
   effect = models.CharField(max_length=150,blank=True,null=True)
   aftereffect = models.CharField(max_length=150,blank=True,null=True)
   trigger = models.CharField(max_length=150,blank=True,null=True)
 
   
   def __unicode__(self):
      return "%s (%s %s power)" % (self.name, self.monster, self.usage)

   def atkRangeDisplay(self):
      str = "" 

      if self.aura:
         str = "Aura %s" % self.area

      elif self.area == 0:
         if self.range == 0:
            str = "Personal"
         else:
            if self.isRanged:
               str = "Ranged %s" % self.range
            else:
               str = "Melee / Touch" if self.range == 1 else "Reach %s" % self.range
      else:
         if self.range == 0:
            str = "Close Burst %s" % self.area
         elif self.range == 1:
            str = "Close Blast %s" % self.area
         else:
            str = "Area Burst %s in %s" % (self.area, self.range)
      if self.oaFlag:
         str += " (Provokes OA)"

      return str
   
   def atkUsageDisplay(self):
      str = "Passive" if self.isPassive else "%s -- %s" % (self.usage, self.get_action_display())
      
      if self.bloodiedLimit:
         str += " (Usable only when bloodied)"
      return str 

   class Meta:
      abstract = True

class Ability(PowerBase):
   pass

class Attack(PowerBase):
   attackBonus = models.IntegerField()
   targetDefense = models.CharField(max_length=1,choices=choices.DEFENSES,verbose_name='Target defense') 
   averageDamage = models.IntegerField()
   damageLine = models.CharField(max_length=150)
   multiStrike = models.BooleanField()
   onHit = models.CharField(max_length=150,blank=True,null=True)
    
   def __unicode__(self):
      return "%s (%s %s)" % (self.name, self.usage, self.action)
   
   def __rebalance__(self):
         self.attackBonus = bhelpers.toHit(self.monster,self.range, self.area, self.isRanged, self.targetDefense)
         hasEffect = True if self.effect or self.aftereffect or self.onHit else False  
         self.averageDamage = bhelpers.averageDamage(self.monster.level,self.monster.minion,self.monster.role.heavyHitter,self.range,self.area,self.usage.limitedUsage,self.multiStrike,hasEffect)
         self.damageLine = bhelpers.damageToDice(self.averageDamage,self.monster.minion,self.onHit)
         self.save()
    
