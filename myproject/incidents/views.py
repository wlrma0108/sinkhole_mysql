from django.shortcuts import render, redirect, get_object_or_404
from .models import Incident
from .forms import IncidentForm
from django.http import JsonResponse
from django.core.serializers import serialize


def incident_geojson(request):
    qs = Incident.objects.select_related('priority','district')
    geojson = {
        "type":"FeatureCollection",
        "features":[
            {
                "type":"Feature",
                "geometry":{
                    "type":"Point",
                    "coordinates":[inc.district.lng, inc.district.lat]
                },
                "properties":{
                    "id":inc.id,
                    "priority":inc.priority.level_name
                }
            } for inc in qs
        ]
    }
    return JsonResponse(geojson)


def incident_list(request):
    qs = Incident.objects.order_by('-date_reported')
    return render(request, 'incidents/list.html', {'incidents': qs})

def incident_create(request):
    if request.method=='POST':
        form = IncidentForm(request.POST, request.FILES)
        if form.is_valid():
            inc = form.save(commit=False)
            inc.reporter = request.user
            inc.save()
            return redirect('incidents:list')
    else:
        form = IncidentForm()
    return render(request, 'incidents/form.html', {'form': form})

def incident_detail(request, pk):
    inc = get_object_or_404(Incident, pk=pk)
    return render(request, 'incidents/detail.html', {'inc': inc})

def incident_update(request, pk):
    inc = get_object_or_404(Incident, pk=pk)
    form = IncidentForm(request.POST or None, request.FILES or None, instance=inc)
    if form.is_valid():
        form.save()
        return redirect('incidents:detail', pk=pk)
    return render(request, 'incidents/form.html', {'form': form})
