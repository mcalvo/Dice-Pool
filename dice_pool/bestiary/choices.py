from django.conf import settings

ATTACK_TYPES = (
        ('SME', 'Single Target Melee'),
        ('SRA', 'Single Target Ranged'),
        ('CBU', 'Close Burst'),
        ('CBL', 'Close Blast'),
        ('AER', 'Area Effect Ranged'),
        ('SEL', 'Self'))

DEFENSES = (
        ('A', 'Armor Class'),
        ('F', 'Fortitude'),
        ('R', 'Reflex'),
        ('W', 'Will'),
        ('S', 'Self'))

ACTION = (
        ('ST', 'Standard'),
        ('MO', 'Move'),
        ('MI', 'Minor'),
        ('II', 'Immediate Interrupt'),
        ('IR', 'Immediate Reaction'),
        ('FR', 'Free')
        )

USABILITY = (
        ('AW', 'At Will'),
        ('EN', 'Encounter'),
        ('OB', 'Only when Bloodied'),
        ('R1', 'Recharge on 6'),
        ('R2', 'Recharge on 5 or 6'),
        ('R3', 'Recharge on 4, 5 or 6'))

FACTIONS = (
        ('GEN', 'General Monsters'),
        ('PCS', 'PCs'),
        ('DRW', 'Drow Houses'),
        )

CREATURE_ROLES = (
        ('AR', 'Artillery'),
        ('BR', 'Brute'),
        ('CO', 'Controller'),
        ('LU', 'Lurker'),
        ('SK', 'Skirmisher'),
        ('SO', 'Soldier'),
        )
