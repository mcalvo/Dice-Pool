from django.core.exceptions import ValidationError
from django.db import models
from django import forms
from django.forms import ModelForm
from bestiary import choices
import math, random

class Mon(models.Model):
    name = models.CharField(max_length = 50)
    level = models.IntegerField()
    role = models.CharField(max_length = 2, choices=choices.CREATURE_ROLES)
    faction = models.CharField(max_length=20, choices = choices.FACTIONS, default="General")
    soloFlag = models.BooleanField(verbose_name = 'Solo?')
    eliteFlag = models.BooleanField(verbose_name = 'Elite?')
    minionFlag = models.BooleanField(verbose_name = 'Minion?')
    init = models.IntegerField(verbose_name = 'Initiative')
    speed = models.IntegerField(verbose_name = 'Speed')
    hp = models.IntegerField(verbose_name = 'Health')
    suddenDmg = models.IntegerField(verbose_name = 'Sudeen Damage Threshold')
    ac = models.IntegerField(verbose_name = 'Armor Class')
    fort = models.IntegerField(verbose_name = 'Fortitude')
    ref = models.IntegerField(verbose_name = 'Reflex')
    will = models.IntegerField(verbose_name = 'Will')
    acAtk = models.IntegerField(verbose_name = 'Attacks vs. AC')
    nacAtk = models.IntegerField(verbose_name = 'Attacks vs. NAD')
    eDC = models.IntegerField(verbose_name = 'Easy DC')
    mDC = models.IntegerField(verbose_name = 'Medium DC')
    hDC = models.IntegerField(verbose_name = 'Hard DC')
    
    def __unicode__(self):
        return self.name

class Attack(models.Model):
    creature = models.ForeignKey(Mon)
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
