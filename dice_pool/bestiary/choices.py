from django.conf import settings

DEFENSES = (
         ('A', 'Armor Class'),
         ('F', 'Fortitude'),
         ('R', 'Reflex'),
         ('W', 'Will'),
         ('M', 'Multiple'),    
         ('S', 'Self')
         )

ACTION = (
         ('ST', 'Standard'),
         ('MO', 'Move'),
         ('MI', 'Minor'),
         ('II', 'Immediate Interrupt'),
         ('IR', 'Immediate Reaction'),
         ('FR', 'Free')
         )

USAGE = (
         ('AW', 'At Will'),
         ('EN', 'Encounter'),
         ('RE', 'Recharge'),
        )

"""
CREATURE_ROLES = (
        ('AR', 'Artillery'),
        ('BR', 'Brute'),
        ('CO', 'Controller'),
        ('LU', 'Lurker'),
        ('SK', 'Skirmisher'),
        ('SO', 'Soldier'),
        )
   #HP Base/HP per Level
   if role == u'AR': hp = math.ceil(24+(3.5*level))
   if role == u'BR': hp = math.ceil(32+(6.5*level))
   if role == u'CO': hp = math.ceil(28+(5.5*level))
   if role == u'LU': hp = math.ceil(24+(3.5*level))
   if role == u'SK': hp = math.ceil(28+(5.5*level))
   if role == u'SO': hp = math.ceil(29+(5.5*level))
   #AC   
   if role == u'AR': return 14+random.randint(-1,2)+level
   if role == u'BR': return 14+random.randint(-2,1)+level
   if role == u'CO': return 14+random.randint(-1,2)+level
   if role == u'LU': return 14+random.randint(-3,1)+level
   if role == u'SK': return 14+random.randint(-1,2)+level
   if role == u'SO': return 14+random.randint(0,3)+level

   #Fortitude
   if role == u'AR': return 12+random.randint(-3,1)+level
   if role == u'BR': return 12+random.randint(1,3)+level
   if role == u'CO': return 12+random.randint(-1,2)+level
   if role == u'LU': return 12+random.randint(-2,1)+level
   if role == u'SK': return 12+random.randint(-1,2)+level
   if role == u'SO': return 12+random.randint(0,2)+level
   
   #Reflex
   if role == u'AR': return 12+random.randint(1,3)+level
   if role == u'BR': return 12+random.randint(-1,2)+level
   if role == u'CO': return 12+random.randint(-1,2)+level
   if role == u'LU': return 12+random.randint(1,3)+level
   if role == u'SK': return 12+random.randint(1,3)+level
   if role == u'SO': return 12+random.randint(0,2)+level
   
   #Will
   if role == u'AR': return 12+random.randint(-1,2)+level
   if role == u'BR': return 12+random.randint(-1,2)+level
   if role == u'CO': return 12+random.randint(1,3)+level
   if role == u'LU': return 12+random.randint(-1,2)+level
   if role == u'SK': return 12+random.randint(-1,2)+level
   if role == u'SO': return 12+random.randint(0,2)+level

   #GibRatio  
   if minionFlag: return health
   if soloFlag: return health * .43
   if eliteFlag: return health * .41
   if role == u'AR': return health * .35
   if role == u'BR': return health * .3
   if role == u'CO': return health * .35
   if role == u'LU': return health * .35
   if role == u'SK': return health * .36
   if role == u'SO': return health * .4
 
"""

