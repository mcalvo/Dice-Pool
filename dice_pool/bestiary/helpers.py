import math, random

def hpCalc(level, role, minion, elite, solo):
   if minion: 
      return 1

   if solo: 
      return math.ceil((level+9)+(6*level)*5+20)
     
   hp = math.ceil(role.hpBase + (role.hpRatio * level))

   if elite:
     hp = math.ceil((hp*1.10)+(level*1.5)+10)
    
   return hp

def defenseCalc(defBase, modMin, modMax, level):
   random.seed()
   return defBase+random.randint(modMin, modMax)+level
   
def gibCalc(hp, ratio, minion, elite, solo):
   if minion: 
      return hp
   elif solo: 
      return int(math.ceil(hp * .43))
   elif elite: 
      return int(math.ceil(hp * .41))
   else: 
      return int(math.ceil(hp * ratio))

def toHit(monster, range, area, isRanged, targetDefense):
   atkBonus = monster.acAtkBase if targetDefense == 'A' else monster.nacAtkBase

   if range > 1 and isRanged and not monster.role.heavyHitter:
      atkBonus = atkBonus + level/10
   
   if monster.solo:
      atkBonus = atkBonus + 2
   
   if eliteFlag:
      atkBonus = atkBonus + 1

   return atkBonus
    
def damageToDice(damage,minion, onHit):
   if minion:
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

def averageDamage(level,minion,heavyHitter,range,area,limited,multiStrike,hasEffect):
   dmg = 0

   if minion:
      dmg = 3 * (level/4) + 3 if heavyHitter else (level/2) + 2
    
   #Brute damage
   else:
      if heavyHitter:
         if limited:
            #limited single target attack vs limited area attack
            dmg = 8+round((level+8)*.9678) if area == 0 else 8+round((level+4)*.9678)
         else:
            #At-will single target attack vs at-will area attack 
            dmg = 8+round((level+3)*.9678) if area == 0 else 8+round((level-1)*.9678)
          
      #Non-brute damage
      else:
         if limited:
            #limited single target attack vs limited AoE attack
            dmg = 8+round((level+5)*.9678) if area == 0 else 8+round(level*.9678)

         else:
            #At-will single target attack vs At-will AoE attack
            dmg = 8+round(level*.9678) if area == 0 else 8+round((level-5)*.9678)
  
   if multiStrike:
      dmg = round(.65*dmg)
   
   if hasEffect:
      dmg = round(.8*dmg)
   
   return int(dmg)
