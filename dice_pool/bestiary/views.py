from django.shortcuts import render_to_response, get_object_or_404, render, redirect
from django.core.urlresolvers import reverse
from django.template import RequestContext
from bestiary import models as mcm 
from bestiary import forms as mcf
import math, random, unicodedata

def monster_listing(request):
    monster_list = mcm.Monster.objects.all().order_by('level')
    return render(request, 'bestiary/mon_list.html', {'monster_list': monster_list})
   
def monster_detail(request, id):
    monster = get_object_or_404(mcm.Monster, id=id)
    return render(request, 'bestiary/mon_detail.html', {'mon': monster})

def create_monster(request, id=None, monster=None):
   if id and not monster:
	   monster = mcm.Mon.objects.get(id=id)

	form = mcf.MonsterForm(request.POST or monster)

	if form.is_valid():
      return redirect(reverse('bestiary_mon_listing'))
	else: 
      return render(request, 'bestiary/mon_create.html', {'form': form,})

def create_power(request,mon_id,power_id=None,power=None):
   monster = mcm.Monster.objects.get(id=mon_id)
	if power_id and not power:
		power = mcm.Attack.objects.get(id=power_id)

	form = mcf.AttackForm(c, request.POST or power)
   
   if form.is_valid():
      form.save()
      return redirect(reverse('bestiary_mon_detail', args =(mon_id,)))
   else: 
      return render(request, 'bestiary/power_create.html', {'form': form, 'c': monster})
