import django_filters
from .models import Campaign, Envelope, Pledge

class CampaignFilter(django_filters.FilterSet):
    name = django_filters.CharFilter(lookup_expr='icontains')
    desc = django_filters.CharFilter(lookup_expr='icontains')
    title = django_filters.CharFilter(lookup_expr='icontains')
    notes = django_filters.CharFilter(lookup_expr='icontains')
    start_date = django_filters.NumberFilter(name='start_date', lookup_expr='year')
    start_date_year__gt = django_filters.NumberFilter(name='start_date', lookup_expr='year__gt')
    start_date_year__lt = django_filters.NumberFilter(name='start_date', lookup_expr='year__lt')
    end_date = django_filters.NumberFilter(name='end_date', lookup_expr='year')
    end_date_year__gt = django_filters.NumberFilter(name='end_date', lookup_expr='year__gt')
    end_date_year__lt = django_filters.NumberFilter(name='end_date', lookup_expr='year__lt')
    class Meta:
        model = Campaign
        fields = ('name', 'desc', 'title', 'notes', 'start_date', 'end_date')

class EnvelopeFilter(django_filters.FilterSet):
    name = django_filters.CharFilter(lookup_expr='icontains')
    desc = django_filters.CharFilter(lookup_expr='icontains')
    class Meta:
        model = Envelope
        fields = ('name', 'desc', 'belongs_to')

class PledgeFilter(django_filters.FilterSet):
    name = django_filters.CharFilter(lookup_expr='icontains')
    start_date = django_filters.NumberFilter(name='start_date', lookup_expr='year')
    #start_date_year__gt = django_filters.NumberFilter(name='start_date', lookup_expr='year__gt')
    #start_date_year__lt = django_filters.NumberFilter(name='start_date', lookup_expr='year__lt')
    end_date = django_filters.NumberFilter(name='end_date', lookup_expr='year')
    #end_date_year__gt = django_filters.NumberFilter(name='end_date', lookup_expr='year__gt')
    #end_date_year__lt = django_filters.NumberFilter(name='end_date', lookup_expr='year__lt')
    class Meta:
        model = Pledge
        fields =("name", "belongs_to", "is_from_contact", "is_from_company", "payments", "payments_cycle", "amount", "total", "recurring", "start_date", "end_date")
