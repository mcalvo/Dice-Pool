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

def defCalc(defBase, modMin, modMax, level):
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
