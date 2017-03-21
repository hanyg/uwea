import django_tables2 as tables
from django_tables2.utils import A

from .models import Campaign, Envelope

class CampaignTable(tables.Table):
    name = tables.LinkColumn('campaign_detail', args=[A('pk')])
    class Meta:
        model = Campaign
        fields =("name", "desc", "start_date", "end_date")
        # add class="paleblue" to <table> tag
        attrs = {'class': 'paleblue'}

class EnvelopeTable(tables.Table):
    name = tables.LinkColumn('envelope_detail', args=[A('pk')])
    class Meta:
        model = Envelope
        fields =("name", "desc", "belongs_to")
        # add class="paleblue" to <table> tag
        attrs = {'class': 'paleblue'}
