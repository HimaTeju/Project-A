from django import forms
from .models import Event

class EventForm(forms.ModelForm):
    class Meta:
        model = Event
        fields = ['name', 'date', 'is_multi_day']
        widgets = {
            'date': forms.DateInput(attrs={'type': 'date'}),
        }