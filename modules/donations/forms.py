from django import forms

from .models import Envelope, Campaign

class EnvelopeForm(forms.ModelForm):

    class Meta:
        model = Envelope
        fields = ('name', 'desc', 'belongs_to',)

class CampaignForm(forms.ModelForm):

    class Meta:
        model = Campaign
        fields = ('name', 'desc', 'title', 'notes', 'start_date', 'end_date')
