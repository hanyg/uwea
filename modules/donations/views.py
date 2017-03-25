from django.shortcuts import render, get_object_or_404
from django.shortcuts import redirect
from django.utils import timezone
from django.contrib.auth.decorators import login_required
from django_tables2 import RequestConfig
from .filters import CampaignFilter, EnvelopeFilter, PledgeFilter
from .tables import CampaignTable, EnvelopeTable, PledgeTable
from .models import Envelope, Campaign, Pledge
from .forms import EnvelopeForm, CampaignForm, PledgeForm

@login_required
def envelopes(request):
    #envelopes = Envelope.objects.order_by('created_on')
    filter = EnvelopeFilter(request.GET, queryset=Envelope.objects.all())
    table = EnvelopeTable(filter.qs)
    RequestConfig(request, paginate={'per_page': 25}).configure(table)
    return render(request, 'envelopes/envelopes.html', { 'table': table, 'filter': filter })

@login_required
def envelope_detail(request, pk):
    e = get_object_or_404(Envelope, pk=pk)
    return render(request, 'envelopes/envelope_detail.html', {'e': e})

@login_required
def envelope_new(request):
    if request.method == "POST":
        form = EnvelopeForm(request.POST)
        if form.is_valid():
            e = form.save(commit=False)
            e.created_by = request.user
            e.created_on = timezone.now()
            e.last_modified_on = timezone.now()
            e.save()
        return render(request, 'envelopes/envelopes.html', {'form': form})
    else:
        form = EnvelopeForm()
    return render(request, 'envelopes/envelope_edit.html', {'form': form})

@login_required
def envelope_edit(request, pk):
    envelope = get_object_or_404(Envelope, pk=pk)
    if request.method == "POST":
        form = EnvelopeForm(request.POST, instance=envelope)
        if form.is_valid():
            envelope = form.save(commit=False)
            envelope.created_by = request.user
            envelope.created_on = timezone.now()
            envelope.last_modified_on = timezone.now()
            envelope.save()
        return render(request, 'envelopes/envelopes.html', {'form': form})
    else:
        form = EnvelopeForm(instance=envelope)
    return redirect('envelopes/envelope_edit.html', pk=envelope.pk)

@login_required
def campaigns(request):
    #campaigns = Campaign.objects.order_by('created_on')
    filter = CampaignFilter(request.GET, queryset=Campaign.objects.all())
    table = CampaignTable(filter.qs)
    RequestConfig(request, paginate={'per_page': 25}).configure(table)
    return render(request, 'campaigns/campaigns.html', { 'table': table, 'filter': filter })

@login_required
def campaign_detail(request, pk):
    c = get_object_or_404(Campaign, pk=pk)
    return render(request, 'campaigns/campaign_detail.html', {'c': c})

@login_required
def campaign_new(request):
    if request.method == "POST":
        form = CampaignForm(request.POST)
        if form.is_valid():
            c = form.save(commit=False)
            c.created_by = request.user
            c.created_on = timezone.now()
            c.last_modified_on = timezone.now()
            c.save()
            filter = CampaignFilter(request.GET, queryset=Campaign.objects.all())
            table = CampaignTable(filter.qs)
            RequestConfig(request, paginate={'per_page': 25}).configure(table)
            return render(request, 'campaigns/campaigns.html', { 'table': table, 'filter': filter })
    else:
        form = CampaignForm()
    return render(request, 'campaigns/campaign_edit.html', {'form': form})

@login_required
def campaign_edit(request, pk):
    campaign = get_object_or_404(Campaign, pk=pk)
    if request.method == "POST":
        form = CampaignForm(request.POST, instance=campaign)
        if form.is_valid():
            campaign = form.save(commit=False)
            campaign.created_by = request.user
            campaign.created_on = timezone.now()
            campaign.last_modified_on = timezone.now()
            campaign.save()
            return redirect('campaigns/campaigns.html')
    else:
        form = CampaignForm(instance=campaign)
    return render(request, 'campaigns/campaign_edit.html', {'form': form})

@login_required
def pledges(request, pk):
    if pk is None:
      filter = PledgeFilter(request.GET, queryset=Pledge.objects.all())
    else:
      filter = PledgeFilter(request.GET, queryset=Pledge.objects.filter(belongs_to=pk))
    table = PledgeTable(filter.qs)
    RequestConfig(request, paginate={'per_page': 25}).configure(table)
    #form = PledgeFilterForm(request.POST)
    return render(request, 'pledges/pledges.html', { 'table': table, 'filter': filter })

@login_required
def pledge_detail(request, pk):
    #c = get_object_or_404(Pledge, pk=pk)
    filter = PledgeFilter(request.GET, queryset=Pledge.objects.filter(pk = pk))
    table = PledgeTable(filter.qs)
    return render(request, 'pledges/pledge_detail.html', {'table': table, 'filter': filter})

@login_required
def pledge_new(request):
    if request.method == "POST":
        form = PledgeForm(request.POST)
        if form.is_valid():
            c = form.save(commit=False)
            c.created_by = request.user
            c.created_on = timezone.now()
            c.last_modified_on = timezone.now()
            c.save()
            filter = PledgeFilter(request.GET, queryset=Pledge.objects.all())
            table = PledgeTable(filter.qs)
            RequestConfig(request, paginate={'per_page': 25}).configure(table)
            return render(request, 'pledges/pledges.html', { 'table': table, 'filter': filter })
    else:
        form = PledgeForm()
    return render(request, 'pledges/pledge_edit.html', {'form': form})

@login_required
def pledge_edit(request, pk):
    pledge = get_object_or_404(Pledge, pk=pk)
    if request.method == "POST":
        form = PledgeForm(request.POST, instance=pledge)
        if form.is_valid():
            pledge = form.save(commit=False)
            pledge.created_by = request.user
            pledge.created_on = timezone.now()
            pledge.last_modified_on = timezone.now()
            pledge.save()
            return redirect('pledges/pledges.html')
    else:
        form = PledgeForm(instance=pledge)
    return render(request, 'pledges/pledge_edit.html', {'form': form})
