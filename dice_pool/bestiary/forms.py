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
        exclude = ('ac', 'fortitude', 'reflex', 'will', 'initiative', 'hp', 'suddenDmg', 'acAtkBase', 'nacAtkBase', 'eDC', 'mDC', 'hDC',)

""" 
class AttackForm(forms.ModelForm):

    def __init__(self, creature, *args, **kwargs):
        super(AttackForm, self).__init__(*args, **kwargs)
        self.c = creature
        
    def save(self, *args, **kwargs):
        data = super(AttackForm, self).save(commit = False, *args, **kwargs)
        data.monster = self.c
        m = self.c
        if data.tardef == u'A':
            data.atkBonus = toHit(m.acAtk, m.role, m.level, data.attackType, m.soloFlag, m.eliteFlag)
        else:
            data.atkBonus = toHit(m.nacAtk, m.role, m.level, data.attackType, m.soloFlag, m.eliteFlag)
        data.avg_dmg = int(avgDmg(m.role,m.minionFlag,m.level,data.attackType,data.use,data.multi_attack))
        data.damage = dmgCalc(data.avg_dmg, m.minionFlag)
        data.save(*args, **kwargs)

    class Meta:
        model = mcm.Attack
        exclude = ('creature','atkBonus', 'avg_dmg', 'damage')
"""

def toHit(atkBonus, role, level, atkType, soloFlag, eliteFlag):
    if atkType != u'SME':
        if role == u'AR' or role == u'CO' or role == u'LU':
            atkBonus = atkBonus + level/10
    if soloFlag:
        atkBonus = atkBonus + 2
    if eliteFlag:
        atkBonus = atkBonus + 1

    return atkBonus
    
 
def dmgCalc(damage, minionFlag):
    if minionFlag:
        return "%s" % (damage)
    dieType = whichDie(damage)
    num = damage*.7
    den = dieType/2 + .5
    numDie = int(round(num/den))
    staticDamage = int(round(damage*.3))    
    calc = "{0}d{1}+{2}".format(numDie, dieType, staticDamage)
    return calc
    
def whichDie(avgDmg):
    random.seed()
    die = random.randint(2, 5)
    die = die*2
    return  die

def avgDmg(role, minionFlag, level, atkType, usage, multi):
    dmg = 0

    if minionFlag:
        if role == u'BR': return 3 * (level/4) + 3
        else: return level/2 + 2
    if atkType == u'SEL': return 0
    
    #Brute damage
    if role == u'BR':
        if usage == u'AW':
            #At-will single target attack
            if atkType == u'SME' or atkType == u'SRA':
                dmg = 8+round((level+3)*.9678)
            #At-will AoE attack
            else:
                dmg = 8+round((level-1)*.9678)
        else:
            #limited single target attack
            if atkType == u'SME' or atkType == u'SRA':
                dmg = 8+round((level+8)*.9678)
            #limited AoE attack
            else:
                dmg = 8+round((level+4)*.9678)

    #Non-brute damage
    else:
        if usage == u'AW':
            #At-will single target attack
            if atkType == u'SME' or atkType == u'SRA':
                dmg = 8+round(level*.9678)
            #At-will AoE attack
            else:
                dmg = 8+round((level-5)*.9678)
        else:
            #limited single target attack
            if atkType == u'SME' or atkType == u'SRA':
                dmg = 8+round((level+5)*.9678)
            #limited AoE attack
            else:
                dmg = 8+round(level*.9678)

    if multi:
        dmg = round(.65*dmg)

    return dmg
