from django.views.decorators.http import require_POST
from django.http import JsonResponse
import json
from incidents.models import Incident
## from .models import Person, IncidentPersonnel,Resource
from django.shortcuts import render
from django.http import JsonResponse
from incidents.models import Incident

def calendar_events(request):
    qs = Incident.objects.exclude(date_resolved__isnull=True)
    events = [{
      'title':f'#{inc.id} - {inc.priority.level_name}',
      'start':inc.date_reported.isoformat(),
      'end':inc.date_resolved.isoformat()
    } for inc in qs]
    return JsonResponse(events, safe=False)

def stock_overview(request):
    resources = Resource.objects.all()
    return render(request, 'resources/stock.html', {'resources':resources}
                  
@require_POST
def assign_person(request, incident_id):
    data = json.loads(request.body)
    IncidentPersonnel.objects.create(
        incident_id=incident_id,
        person_id=data['person_id'],
        role='현장 복구요원'
    )
    return JsonResponse({'status':'ok'})