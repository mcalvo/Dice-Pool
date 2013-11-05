from django.contrib import messages
from django.shortcuts import render_to_response, get_object_or_404, render, redirect
from django.core.urlresolvers import reverse
from django.template import RequestContext
from bestiary import models as mcm 
from bestiary import forms as mcf
import math, random, unicodedata

def monsterListing(request):
   monster_list = mcm.Monster.objects.all().order_by('level')
   return render(request, 'bestiary/monsterList.html', {'monster_list': monster_list})
   
def monsterDetail(request, mon_id):
   monster = get_object_or_404(mcm.Monster, id=mon_id)
   return render(request, 'bestiary/monsterDetail.html', {'mon': monster})

def editMonster(request, mon_id=None, monster=None):
   if mon_id and not monster:
	   monster = mcm.Mon.objects.get(id=mon_id)
   
   form = mcf.MonsterForm(request.POST or monster)
   
   if form.is_valid():
      form.save()
      return redirect(reverse('bestiary_monsterListing'))
   return render(request, 'bestiary/monsterCreate.html', {'form': form,})

def editAbility(request,mon_id,form=None,attack_id=None, ability_id=None):
   try:   
      monster = mcm.Monster.objects.get(id=mon_id)
   except mcm.Monster.DoesNotExist:
      messages.error(request, "Not a valid monster.")
      return redirect(reverse('bestiary_monsterListing'))
   
   refObj=None 
   
   try:
      if attack_id:
         refObj = mcm.Attack.objects.get(id=attack_id)
      if ability_id:
         refObj = mcm.Ability.objects.get(id=ability_id)
   except mcm.Attack.DoesNotExist:
      messages.error(request, "No valid attack referenced.")
      return redirect(reverse('bestiary_monsterDetail', {'mon_id': mon_id,}))
   except mcm.Ability.DoesNotExist:
      messages.error(request, "No valid ability referenced.")
      return redirect(reverse('bestiary_monsterDetail', {'mon_id': mon_id,}))
   
   reqForm = form(monster, request.POST or refObj)
   if request.POST and reqForm.is_valid():
      reqForm.save()
      return redirect(reverse('bestiary_monsterDetail', args=[mon_id,]))

   return render(request, 'bestiary/editAbility.html', {'form': reqForm, 'c': monster})
