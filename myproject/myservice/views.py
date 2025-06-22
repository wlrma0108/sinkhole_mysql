from django.shortcuts import render, get_object_or_404, redirect
from .models import Incident
from .forms import IncidentForm

def incident_list(request):
    qs = Incident.objects.all().order_by('-date_reported')
    return render(request, 'sinkhole/incident_list.html', {'incidents': qs})

def incident_detail(request, pk):
    inc = get_object_or_404(Incident, pk=pk)
    return render(request, 'sinkhole/incident_detail.html', {'incident': inc})

def incident_create(request):
    if request.method == 'POST':
        form = IncidentForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('incident_list')
    else:
        form = IncidentForm()
    return render(request, 'sinkhole/incident_form.html', {'form': form})
