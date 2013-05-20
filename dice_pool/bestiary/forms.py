from django.core.exceptions import ValidationError
from django.db import models
from django import forms
from django.forms import ModelForm
from bestiary import choices
from bestiary import models as mcm
import math, random

# Create the form for USER monster creation
class MonForm(ModelForm):
    level = forms.IntegerField(label='Level', min_value=1, max_value=50)

    def save(self, *args, **kwargs):
        data = super(MonForm, self).save(commit = False, *args, **kwargs)
        if data:
            random.seed()
            data.init = data.level*.60
            data.hp = hpCalc(data.minionFlag, data.soloFlag, data.eliteFlag, data.role, data.level)
            data.suddenDmg = suddenDmgThresh(data.soloFlag, data.eliteFlag, data.minionFlag, data.role, data.hp)
            data.ac = acCalc(data.role, data.level)
            data.fort = fCalc(data.role, data.level)
            data.ref = rCalc(data.role, data.level)
            data.will = wCalc(data.role, data.level)
            data.acAtk = random.randint(-1,1)+ 5 + data.level
            data.nacAtk = random.randint(-1,1) + 3 + data.level
            #Calculate skill levels
            data.eDC = 7 + round(data.level * .53)
            data.mDC = 12 + round(data.level * .53) + round(data.level/10)
            data.hDC = 17 + round(data.level * .64) + round(data.level/5)
        data.save(*args, **kwargs)

    class Meta:
        model = mcm.Mon
        fields = ('name', 'level', 'role', 'minionFlag', 'eliteFlag', 'soloFlag', 'speed')
        exclude = ('ac', 'fort', 'ref', 'will', 'init', 'hp', 'suddenDmg', 'acAtk', 'nacAtk', 'eDC', 'mDC', 'hDC',)
    
class AttackForm(ModelForm):

    def __init__(self, creature, *args, **kwargs):
        super(AttackForm, self).__init__(*args, **kwargs)
        self.c = creature
        
    def save(self, *args, **kwargs):
        data = super(AttackForm, self).save(commit = False, *args, **kwargs)
        data.creature = self.c
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

def hpCalc(minionFlag, soloFlag, eliteFlag, role, level):
    if minionFlag: return 1

    if soloFlag: return math.ceil((level+9)+(6*level)*5+20)
    
    if role == u'AR': hp = math.ceil(24+(3.5*level))
    if role == u'BR': hp = math.ceil(32+(6.5*level))
    if role == u'CO': hp = math.ceil(28+(5.5*level))
    if role == u'LU': hp = math.ceil(24+(3.5*level))
    if role == u'SK': hp = math.ceil(28+(5.5*level))
    if role == u'SO': hp = math.ceil(29+(5.5*level))
    
    if eliteFlag: hp = round((hp*1.10)+(level*1.5)+10)
    
    return hp

def acCalc(role, level):
    random.seed()
    #Implement bonuses to Solo and Elite defenses   
    if role == u'AR': return 14+random.randint(-1,2)+level
    if role == u'BR': return 14+random.randint(-2,1)+level
    if role == u'CO': return 14+random.randint(-1,2)+level
    if role == u'LU': return 14+random.randint(-3,1)+level
    if role == u'SK': return 14+random.randint(-1,2)+level
    if role == u'SO': return 14+random.randint(0,3)+level

def fCalc(role, level):
    random.seed()
    #Implement bonuses to Solo and Elite defenses   
    if role == u'AR': return 12+random.randint(-3,1)+level
    if role == u'BR': return 12+random.randint(1,3)+level
    if role == u'CO': return 12+random.randint(-1,2)+level
    if role == u'LU': return 12+random.randint(-2,1)+level
    if role == u'SK': return 12+random.randint(-1,2)+level
    if role == u'SO': return 12+random.randint(0,2)+level

def rCalc(role, level):
    random.seed()
    #Implement bonuses to Solo and Elite defenses
    if role == u'AR': return 12+random.randint(1,3)+level
    if role == u'BR': return 12+random.randint(-1,2)+level
    if role == u'CO': return 12+random.randint(-1,2)+level
    if role == u'LU': return 12+random.randint(1,3)+level
    if role == u'SK': return 12+random.randint(1,3)+level
    if role == u'SO': return 12+random.randint(0,2)+level

def wCalc(role, level):
    random.seed()
    #Implement bonuses to Solo and Elite defenses
    if role == u'AR': return 12+random.randint(-1,2)+level
    if role == u'BR': return 12+random.randint(-1,2)+level
    if role == u'CO': return 12+random.randint(1,3)+level
    if role == u'LU': return 12+random.randint(-1,2)+level
    if role == u'SK': return 12+random.randint(-1,2)+level
    if role == u'SO': return 12+random.randint(0,2)+level

def toHit(atkBonus, role, level, atkType, soloFlag, eliteFlag):
    if atkType != u'SME':
        if role == u'AR' or role == u'CO' or role == u'LU':
            atkBonus = atkBonus + level/10
    if soloFlag:
        atkBonus = atkBonus + 2
    if eliteFlag:
        atkBonus = atkBonus + 1

    return atkBonus
    
def suddenDmgThresh(soloFlag, eliteFlag, minionFlag, role, health):
    if minionFlag: return health
    if soloFlag: return health * .43
    if eliteFlag: return health * .41
    if role == u'AR': return health * .35
    if role == u'BR': return health * .3
    if role == u'CO': return health * .35
    if role == u'LU': return health * .35
    if role == u'SK': return health * .36
    if role == u'SO': return health * .4
  
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
