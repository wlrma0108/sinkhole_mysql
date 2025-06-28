from django.shortcuts import render, redirect, get_object_or_404
from .models import SinkholeIncident
from django.db.models import Sum, Count
from django.db.models.functions import TruncMonth
from django.shortcuts import render
from .forms import IncidentForm 

def incident_list(request):
    incidents = SinkholeIncident.objects.all()
    return render(request, 'sinkhole/incident_list.html', {'incidents': incidents})
def stats_view(request):
    # (A) 사고별 총 자재 사용량
    incident_stats = SinkholeIncident.objects.annotate(
        total_usage=Sum('materials__quantity')
    )
    # incident_stats 각 원소: .id, .date, .location 등 기본 필드 + .total_usage 속성

    # (B) 월별 자재 사용량·사고 건수
    monthly_stats = (
        SinkholeIncident.objects
        .annotate(month=TruncMonth('date'))     # date 필드를 YYYY-MM 으로 자름
        .values('month')                        # month 필드만 남기고 그룹화
        .annotate(
            total_usage=Sum('materials__quantity'),
            incident_count=Count('id')
        )
        .order_by('month')
    )
    # monthly_stats 각 원소: 'month', 'total_usage', 'incident_count'

    return render(request, 'sinkhole/stats.html', {
        'incident_stats': incident_stats,
        'monthly_stats': monthly_stats
    })
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