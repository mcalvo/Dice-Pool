# Create your views here.
from django.shortcuts import render_to_response, get_object_or_404, render
from django.core.urlresolvers import reverse
from django.http import HttpResponseRedirect, HttpResponse
from django.template import RequestContext
from bestiary import models as mcm 
from bestiary import forms as mcf
import math, random, unicodedata

def index(request):
    monster_list = mcm.Mon.objects.all().order_by('level')
    return render_to_response('bestiary/index.html', {'monster_list': monster_list})
   
def detail(request, mon_id):
    m = get_object_or_404(mcm.Mon, pk=mon_id)
    return render_to_response('bestiary/detail.html', {'mon': m})

def create(request):
    form = mcf.MonForm(request.POST or None)
    
    if form.is_valid():
        form.save()
        return HttpResponseRedirect(reverse('bestiary_mon_listing'))
    else: return render(request, 'bestiary/create.html', {'form': form,})

def power(request, mon_id):
    c = mcm.Mon.objects.get(id = mon_id)
    form = mcf.AttackForm(c, request.POST or None,)
    if form.is_valid():
        form.save()
        return HttpResponseRedirect(reverse('bestiary_mon_detail', args =(mon_id,)))
    else: return render(request, 'bestiary/power.html', {'form': form, 'c': c})
