from django.template import Library
import re
register = Library()

@register.simple_tag
def damageLineRollCall(damageLine):
   rollPattern = re.compile("([0-9]*)d([0-9]+|%)([0-9,+,-]*)") 
   breaks = rollPattern.search(damageLine)
   if breaks is None:
      return "%s , +0" % damageLine
   breaks = breaks.groups()
   if len(breaks) == 2:
      breaks.append("+ 0")
   return 'dice.d%s(%s, true), %s' % (breaks[1], breaks[0], breaks[2])
