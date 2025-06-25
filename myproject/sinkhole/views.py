from django.shortcuts import render, redirect, get_object_or_404
from .models import SinkholeIncident
from .forms import IncidentForm  # 모델 폼 가정

def incident_list(request):
    incidents = SinkholeIncident.objects.all()
    return render(request, 'sinkhole/incident_list.html', {'incidents': incidents})

def incident_create(request):
    if request.method == 'POST':
        form = IncidentForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('incident_list')
    else:
        form = IncidentForm()
    return render(request, 'sinkhole/incident_form.html', {'form': form})

def incident_update(request, pk):
    incident = get_object_or_404(SinkholeIncident, pk=pk)
    if request.method == 'POST':
        form = IncidentForm(request.POST, instance=incident)
        if form.is_valid():
            form.save()
            return redirect('incident_list')
    else:
        form = IncidentForm(instance=incident)
    return render(request, 'sinkhole/incident_form.html', {'form': form})

def incident_delete(request, pk):
    incident = get_object_or_404(SinkholeIncident, pk=pk)
    incident.delete()
    return redirect('incident_list')