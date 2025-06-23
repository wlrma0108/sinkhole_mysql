from django import forms
from ..myproject.models import Incident

class IncidentForm(forms.ModelForm):
    class Meta:
        model = Incident
        fields = ['district', 'date_reported', 'date_resolved', 'width', 'depth']
