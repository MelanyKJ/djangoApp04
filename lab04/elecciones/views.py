from django.shortcuts import get_object_or_404,render
from  django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse
from  .models import Region, Candidato
# Create your views here.

def index(request):
    regiones = Region.objects.all()
    context = {
        'regiones': regiones
    }
    return render(request,'elecciones/index.html', context)

def candidatos(request,region_id):
    regiones_r = get_object_or_404(Region,pk=region_id)
    return render(request,'elecciones/candidatos.html', {'regiones_r':regiones_r})

def detalle(request,region_id):
    candidato = get_object_or_404(Candidato, pk=region_id)
    return render(request,'elecciones/detalle.html',{'candidato':candidato})
