import math, random

def hpCalc(level, role, minion, elite, solo):
   if minion: 
      return 1

   if solo: 
      return math.ceil((level+9)+(6*level)*5+20)
     
   hp = math.ceil(role.hpBase + (role.hpRatio * level))

   if elite:
     hp = math.ceil((hp*1.10)+(level*1.5)+10)
    
   return int(hp)

def defenseCalc(defBase, modMin, modMax, level, elite, solo):
   random.seed()
   if solo:
      defBase += 2
   if elite:
      defBase += 2
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
      atkBonus = atkBonus + monster.level/10
   
   if area > 0:
      atkBonus = atkBonus - 1 
 
   if monster.solo:
      atkBonus = atkBonus + 2
   
   if monster.elite:
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
   die = random.randint(3, 5)
   die = die*2
   return  die

def averageDamage(monster,heavyHitter,range,area,limitedUsage,bloodiedLimit,multiStrike,hasEffect):
   dmg = 0

   if monster.minion:
      dmg = 3 * (monster.level/4) + 3 if heavyHitter else (monster.level/2) + 2
    
   #Brute damage
   else:
      if heavyHitter:
         if limitedUsage:
            #limited single target attack vs limited area attack
            dmg = 8+round((monster.level+8)*.9678) if area == 0 else 8+round((monster.level+4)*.9678)
         else:
            #At-will single target attack vs at-will area attack 
            dmg = 8+round((monster.level+3)*.9678) if area == 0 else 8+round((monster.level-1)*.9678)
          
      #Non-brute damage
      else:
         if limitedUsage:
            #limited single target attack vs limited AoE attack
            dmg = 8+round((monster.level+5)*.9678) if area == 0 else 8+round(monster.level*.9678)

         else:
            #At-will single target attack vs At-will AoE attack
            dmg = 8+round(monster.level*.9678) if area == 0 else 8+round((monster.level-5)*.9678)
   
   if bloodiedLimit:
      dmg = round(1.5*dmg)
   
   if monster.elite:
      dmg = round(1.2*dmg)

   if monster.solo:
      dmg = round(1.4*dmg)

   if multiStrike:
      dmg = round(.65*dmg)
   
   if hasEffect:
      dmg = round(.8*dmg)
   
   return int(dmg)
