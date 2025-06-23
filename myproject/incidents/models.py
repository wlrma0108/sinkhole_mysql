from django.db import models
from django.conf import settings

class Incident(models.Model):
    district       = models.ForeignKey('resources.District', on_delete=models.PROTECT)
    reporter       = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.SET_NULL, null=True)
    cause          = models.ForeignKey('resources.CauseType', on_delete=models.SET_NULL, null=True)
    priority       = models.ForeignKey('resources.PriorityLevel', on_delete=models.SET_NULL, null=True)
    status         = models.CharField(max_length=20, default='신고됨')
    date_reported  = models.DateTimeField(auto_now_add=True)
    date_resolved  = models.DateTimeField(blank=True, null=True)
    width          = models.FloatField(blank=True, null=True)
    depth          = models.FloatField(blank=True, null=True)
    photo          = models.ImageField(upload_to='incidents/photos/', blank=True, null=True)
    video          = models.FileField(upload_to='incidents/videos/', blank=True, null=True)

# incidents/forms.py
from django import forms
from .models import Incident

class IncidentForm(forms.ModelForm):
    class Meta:
        model = Incident
        fields = [
            'district','cause','priority','width','depth','photo','video'
        ]
