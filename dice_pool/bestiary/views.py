from django.shortcuts import render_to_response, get_object_or_404, render
from django.core.urlresolvers import reverse
from django.http import HttpResponseRedirect, HttpResponse
from django.template import RequestContext
from bestiary import models as mcm 
from bestiary import forms as mcf
import math, random, unicodedata

def mon_listing(request):
    monster_list = mcm.Mon.objects.all().order_by('level')
    return render(request, 'bestiary/mon_list.html', {'monster_list': monster_list})
   
def mon_detail(request, mon_id):
    m = get_object_or_404(mcm.Mon, id=mon_id)
    return render(request, 'bestiary/mon_detail.html', {'mon': m})

def create_mon(request, mon_id=None, mon=None):
	if mon_id and not mon:
		mon = mcm.Mon.objects.get(id=mon_id)

	form = mcf.MonForm(request.POST or mon)

	if form.is_valid():
		return HttpResponseRedirect(reverse('bestiary_mon_listing'))
	else: 
		return render(request, 'bestiary/mon_create.html', {'form': form,})

def create_power(request, mon_id, power_id=None, power=None):
    c = mcm.Mon.objects.get(id = mon_id)
	if power_id and not power:
		power = mcm.Attack.objects.get(id=power_id)

	form = mcf.AttackForm(c, request.POST or power)

    if form.is_valid():
        form.save()
        return HttpResponseRedirect(reverse('bestiary_mon_detail', args =(mon_id,)))
    else: 
		return render(request, 'bestiary/power_create.html', {'form': form, 'c': c})
