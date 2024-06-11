from django import forms
from .models import CircuitDocument

class CircuitDocumentForm(forms.ModelForm):
    class Meta:
        model = CircuitDocument
        fields = ['circuit', 'document']
