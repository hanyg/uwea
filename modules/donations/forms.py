from django import forms

from .models import Envelope

class EnvelopeForm(forms.ModelForm):

    class Meta:
        model = Envelope
        fields = ('name', 'desc', 'belongs_to',)
