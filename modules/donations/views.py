from django.shortcuts import render, get_object_or_404
from django.shortcuts import redirect
from django.utils import timezone
from django.contrib.auth.decorators import login_required

from .models import Envelope, Campaign
from .forms import EnvelopeForm, CampaignForm

@login_required
def envelopes(request):
    envelopes = Envelope.objects.order_by('created_on')
    return render(request, 'envelopes/envelopes.html', { 'envelopes': envelopes })

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
            return redirect('envelope_detail', pk=e.pk)
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
            return redirect('envelope_detail', pk=envelope.pk)
    else:
        form = EnvelopeForm(instance=envelope)
    return render(request, 'envelopes/envelope_edit.html', {'form': form})

@login_required
def campaigns(request):
    campaigns = Campaign.objects.order_by('created_on')
    return render(request, 'campaigns/campaigns.html', { 'campaigns': campaigns })

@login_required
def campaign_detail(request, pk):
    c = get_object_or_404(Campaign, pk=pk)
    return render(request, 'campaigns/campaign_detail.html', {'c': c})

@login_required
def campaign_new(request):
    if request.method == "POST":
        form = EnvelopeForm(request.POST)
        if form.is_valid():
            c = form.save(commit=False)
            c.created_by = request.user
            c.created_on = timezone.now()
            c.last_modified_on = timezone.now()
            c.save()
            return redirect('campaign_detail', pk=c.pk)
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
            return redirect('campaign_detail', pk=campaign.pk)
    else:
        form = CampaignForm(instance=campaign)
    return render(request, 'campaigns/campaign_edit.html', {'form': form})
